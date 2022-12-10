MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

def get_dir(head, tail):
    return 1 if head > tail else -1


def compute_tail_position(head, tail):
    if abs(head[0] - tail[0]) <= 1  and abs(head[1] - tail[1]) <= 1:
        return tail
    elif abs(head[0] - tail[0]) == 2:
        new_tail_x = tail[0] + get_dir(head[0], tail[0])
        new_tail_y = tail[1] + (0 if head[1] == tail[1] else get_dir(head[1], tail[1]))
        return (new_tail_x, new_tail_y)
    else:
        new_tail_x = tail[0] + (0 if head[0] == tail[0] else get_dir(head[0], tail[0]))
        new_tail_y = tail[1] + get_dir(head[1], tail[1])
        return (new_tail_x, new_tail_y)


def get_positions_visited_by_tail(rope_length):
    positions_visited_by_tail = set()
    rope = [(0, 0) for i in range (0, rope_length)]
    tail = rope_length - 1

    for line in open('input-9-1.txt'):
        move_input = line.strip().split(' ')
        move = MOVES[move_input[0]]

        for i in range(0, int(move_input[1])):
            positions_visited_by_tail.add(rope[tail])
            rope[0] = (rope[0][0] + move[0], rope[0][1] + move[1])

            for i in range(1, rope_length):
                rope[i] = compute_tail_position(rope[i - 1], rope[i])

        positions_visited_by_tail.add(rope[tail])
    return len(positions_visited_by_tail)

print(f'the positions visited by tail1={get_positions_visited_by_tail(2)}')
print(f'the positions visited by tail2={get_positions_visited_by_tail(10)}')

