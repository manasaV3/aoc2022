import sys

VISITED = 'V'
topography = []
steps_to_point = {}
start_point, end_point = None, None


def find_position(char, line, index, start_index=0):
    if char in line[start_index:]:
        return index, start_index + line[start_index:].find(char)
    return None


def replace_at_index(line, index, replacement):
    return line[:index] + replacement + line[index + 1:]


def get_topography():
    global topography, start_point, end_point
    input_file = open('input-12-1.txt', 'r')
    index = 0
    while line := input_file.readline():
        clean_line = line.strip()
        if not start_point:
            start_point = find_position('S', clean_line, index)
        if not end_point:
            end_point = find_position('E', clean_line, index)

        topography.append(clean_line)
        index += 1

    topography[start_point[0]] = replace_at_index(topography[start_point[0]], start_point[1], 'a')
    topography[end_point[0]] = replace_at_index(topography[end_point[0]], end_point[1], 'z')


def can_move_to_point(point, visited, height_ord):
    return point not in visited and 0 <= point[0] < len(topography) and 0 <= point[1] < len(topography[point[0]]) and \
           ord(topography[point[0]][point[1]]) <= height_ord + 1


def get_min_path_bfs(start):
    queue = [(start, 0, set())]
    steps_to_point = {}
    while queue:
        point_data = queue.pop(0)
        point = point_data[0]

        if point in steps_to_point:
            continue

        if point == end_point:
            return point_data[1]

        steps_to_point[point] = point_data[1]
        height_ord = ord(topography[point[0]][point[1]])
        point_data[2].add(point)
        path_size = point_data[1] + 1
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new = (point[0] + move[0], point[1] + move[1])
            if can_move_to_point(new, point_data[2], height_ord) and steps_to_point.get(new, sys.maxsize) > path_size:
                queue.append((new, path_size, point_data[2].copy()))

    return sys.maxsize


def get_all_lowest_points():
    lowest_points = []
    for index in range(0, len(topography)):
        start = 0
        while point := find_position('a', topography[index], index, start):
            lowest_points.append(point)
            start = point[1] + 1

    return lowest_points


get_topography()
print(f'min path size from start to end= {get_min_path_bfs(start_point)}')

smallest_path = sys.maxsize
for start in get_all_lowest_points():
    smallest_path = min(get_min_path_bfs(start), smallest_path)

print(f'smallest path from any a to E = {smallest_path}')
