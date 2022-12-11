def process_for_signal_strength(cycle, register):
    global target_cycle, signal_strength
    if cycle == target_cycle:
        signal_strength += cycle * register
        target_cycle = target_cycle + 40

    pixel = (cycle - 1) % 40
    current_pixel = '#' if register in range(pixel - 1,  pixel + 2) else ' '
    print(current_pixel, end = '\n' if cycle % 40 == 0 else '')


input_file = open('input-10-1.txt')

target_cycle = 20
cycle = signal_strength = 0
register = 1

while line := input_file.readline().strip():    
    is_not_noop = line != 'noop'

    for i in range(0, 2 if is_not_noop else 1):
        cycle += 1
        process_for_signal_strength(cycle, register)

    if is_not_noop:
        register += int(line.split(' ')[1])


print(f'\nsignal strength at cycle={cycle} is {signal_strength}')
