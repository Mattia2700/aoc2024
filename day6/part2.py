import os

from tqdm import tqdm


class Directions:
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().splitlines()

map = []
for row in data:
    current = []
    for el in row:
        current.append(el)
    map.append(current)

# get '^' index
start_x, start_y = -1, -1
for i in range(len(map)):
    if '^' in map[i]:
        start_x = i
        start_y = map[i].index('^')
        break

direction = Directions.UP

# get coords with '.'
coords = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '.':
            coords.append((i, j))

total = 0

for a, b in tqdm(coords):
    map[a][b] = '#'

    current_x, current_y = start_x, start_y
    direction = Directions.UP
    visited = []
    loop = False
    new_map = [row.copy() for row in map]

    try:
        for row in new_map:
            if loop:
                break
            for column in row:
                # while not outside boundaries
                if loop:
                    break
                while 0 <= current_x <= len(map) - 1 and 0 <= current_y <= len(map[0]) - 1:

                    if ((current_x, current_y), direction) in visited:
                        loop = True
                        break
                    else:
                        new_map[current_x][current_y] = 'X'
                        visited.append(((current_x, current_y), direction))

                    match direction:
                        case Directions.UP:
                            if new_map[current_x - 1][current_y] != '#':
                                current_x -= 1
                            else:
                                direction = Directions.RIGHT
                        case Directions.DOWN:
                            if new_map[current_x + 1][current_y] != '#':
                                current_x += 1
                            else:
                                direction = Directions.LEFT
                        case Directions.RIGHT:
                            if new_map[current_x][current_y + 1] != '#':
                                current_y += 1
                            else:
                                direction = Directions.DOWN
                        case Directions.LEFT:
                            if new_map[current_x][current_y - 1] != '#':
                                current_y -= 1
                            else:
                                direction = Directions.UP
    except IndexError:
                pass
    map[a][b] = '.'
    if loop:
        total += 1

print(total)