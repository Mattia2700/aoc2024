import os

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
current_x, current_y = -1, -1
for i in range(len(map)):
    if '^' in map[i]:
        current_x = i
        current_y = map[i].index('^')
        break

direction = Directions.UP

# while not outside boundaries
try:
    while 0 <= current_x <= len(map) - 1 and 0 <= current_y <= len(map[0]) - 1:
        map[current_x][current_y] = 'X'

        match direction:
            case Directions.UP:
                if map[current_x - 1][current_y] != '#':
                    current_x -= 1
                else:
                    direction = Directions.RIGHT
            case Directions.DOWN:
                if map[current_x + 1][current_y] != '#':
                    current_x += 1
                else:
                    direction = Directions.LEFT
            case Directions.RIGHT:
                if map[current_x][current_y + 1] != '#':
                    current_y += 1
                else:
                    direction = Directions.DOWN
            case Directions.LEFT:
                if map[current_x][current_y - 1] != '#':
                    current_y -= 1
                else:
                    direction = Directions.UP
except IndexError:
    pass

# count all 'X' in map
count = 0
for row in map:
    for el in row:
        if el == 'X':
            count += 1

print(count)