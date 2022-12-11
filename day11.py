import collections
import math
import re

Monkey = collections.namedtuple('Monkey',
                                ['name', 'items', 'operation', 'test', 'ifTrue', 'ifFalse', 'inspected_count'])


def get_line():
    global input_file
    return input_file.readline().strip()


def get_first_matched_group(regex) -> str:
    return re.match(regex, get_line()).groups()[0]


def parse_file_to_monkeys() -> list[Monkey]:
    global monkeys
    monkeys = []
    while line := get_line():
        monkey = Monkey(
            name=line.strip().lower(),
            items=list(map(int, get_first_matched_group('^Starting items: ([0-9,\\w].*)$').split(', '))),
            operation=get_first_matched_group('^Operation: new = (.*)$'),
            test=int(get_first_matched_group('^Test: divisible by (\\d*)$')),
            ifTrue=int(get_first_matched_group('^If true: throw to monkey (\\d*)$')),
            ifFalse=int(get_first_matched_group('^If false: throw to monkey (\\d*)$')),
            inspected_count=[0],
        )
        monkeys.append(monkey)
        get_line()
    return monkeys


def do_monkey_business(stress_level_updater):
    for monkey in monkeys:
        item_count = len(monkey.items)
        monkey.inspected_count[0] += item_count
        for i in range(0, item_count):
            old = monkey.items.pop(0)
            stress = int(stress_level_updater(eval(monkey.operation)))
            test_outcome = monkey.ifTrue if stress % monkey.test == 0 else monkey.ifFalse
            monkeys[test_outcome].items.append(stress)


def solve(rounds, stress_management):
    global monkeys
    for i in range(0, rounds):
        do_monkey_business(stress_management)

    inspected_counts = [monkey.inspected_count[0] for monkey in monkeys]
    inspected_counts.sort(reverse=True)
    return inspected_counts[0] * inspected_counts[1]


input_file = open('input-11-1.txt', 'r')
parse_file_to_monkeys()
print(f'solution 1={solve(20, lambda x: x / 3)}')

input_file = open('input-11-1.txt', 'r')
parse_file_to_monkeys()
super_modulo = math.prod([monkey.test for monkey in monkeys])
print(f'solution 2={solve(10000, lambda x: x % super_modulo)}')
