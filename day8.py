import math

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_trees_as_matrix():
    input_file = open('input-8-1.txt')
    tree_matrix = []
    while line := input_file.readline():
        tree_row = [int(height) for height in line.strip()]
        tree_matrix.append(tree_row)
    return tree_matrix


def get_distance_in_dir(i, j, dir, trees):
    dx, dy = dir
    distance = 0
    tree_height = trees[i][j]
    i += dx
    j += dy

    while i > -1 and i < m and j > -1 and j < n:
        distance += 1
        if trees[i][j] >= tree_height:
            break
        i += dx
        j += dy

    return distance        


def get_tree_distance(i, j, trees):
    return math.prod([get_distance_in_dir(i, j, dir, trees) for dir in DIRECTIONS])

tree_matrix = get_trees_as_matrix()

m = len(tree_matrix)
n = len(tree_matrix[0])

max_tree_distance = 0
visible_trees = set()
for i in range(0, m):
    max_left = -1
    for j in range(0, n):
        if i == 0 or i == m -1 or j == 0 or j == n-1 or max_left < tree_matrix[i][j]:
            visible_trees.add(i * n + j)
        max_left = max(max_left, tree_matrix[i][j])

        max_tree_distance = max(max_tree_distance, get_tree_distance(i, j, tree_matrix))

    max_right = -1
    for j in range(n - 1, -1, -1):
        if max_right < tree_matrix[i][j]:
            visible_trees.add(i * n + j)
        max_right = max(max_right, tree_matrix[i][j])


for j in range(0, n):
    max_top = -1
    for i in range(0, m):
        if max_top < tree_matrix[i][j]:
            visible_trees.add(i * n + j)
        max_top = max(max_top, tree_matrix[i][j])

    max_bottom = -1
    for i in range(m - 1, -1, -1):
        if max_bottom < tree_matrix[i][j]:
            visible_trees.add(i * n + j)
        max_bottom = max(max_bottom, tree_matrix[i][j])


print(f'Total number of visible trees={len(visible_trees)}')

print(f'Max tree distance={max_tree_distance}')
