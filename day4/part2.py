import os

def is_valid_pattern(grid):
    if not grid[1][1] == 'A':
        return 0

    count = 0

    for rot in range(4):
        if grid[0][0] == 'M' and grid[0][2] == 'M' and grid[2][0] == 'S' and grid[2][2] == 'S':
            count += 1
        # rotate clockwise
        grid = list(zip(*grid[::-1]))

    return count


def find_x(grid):
    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[i]) - 2):
            # create a 3x3 grid
            sub_grid = [grid[i][j:j + 3], grid[i + 1][j:j + 3], grid[i + 2][j:j + 3]]
            count += is_valid_pattern(sub_grid)
    return count

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().splitlines()

grid = []
total = 0

for line in data:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

total += find_x(grid)

print(total)
