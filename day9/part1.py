import os

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read()

disk = []
current = 0
total = 0

for idx, number in enumerate(data):
    if idx % 2 == 0:
        disk.extend(int(data[idx]) * [str(current)])
        current += 1
    else:
        disk.extend(int(data[idx]) * ['.'])

initial_dots = disk.count('.')

left = 0
right = len(disk) - 1

while not all([x == '.' for x in disk[-initial_dots:]]):
    while disk[left] != '.':
        left += 1
    while disk[right] == '.':
        right -= 1

    disk[left] = disk[right]
    disk[right] = '.'

for idx, x in enumerate(disk):
    if x == '.':
        break
    total += idx * int(x)

print(total)