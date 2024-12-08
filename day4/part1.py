import os
import re

def find_horizontal(grid):
    count = 0
    for row in grid:
        current = ''.join(row)
        count += len(re.findall(r'(XMAS)', current))
        count += len(re.findall(r'(SAMX)', current))
    return count

def find_vertical(grid):
    # transpose grid
    transposed = list(map(list, zip(*grid)))
    return find_horizontal(transposed)

def find_diagonal(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i + 3 < len(grid) and j + 3 < len(grid[i]):
                if grid[i][j] == 'X' and grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
                    count += 1

            if i + 3 < len(grid) and j - 3 >= 0:
                if grid[i][j] == 'X' and grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
                    count += 1

    return count

def find_reverse_diagonal(grid):
    # mirror rows
    mirrored = list(reversed(grid))
    return find_diagonal(mirrored)

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().splitlines()

grid = []
total = 0

for line in data:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

total += find_horizontal(grid)
total += find_vertical(grid)
total += find_diagonal(grid)
total += find_reverse_diagonal(grid)

print(total)
