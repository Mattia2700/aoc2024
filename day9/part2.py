import os
import re

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
current_number = '1'
right = len(disk) - 1
# input()

while int(current_number) >= 1:
    left = 0
    current_number_length = 1

    print(''.join(disk))
    input()
    while disk[right] == '.':
        right -= 1
    current_number = disk[right]
    while disk[right-1] == current_number:
        # print(disk[right-1])
        current_number_length += 1
        right -= 1

    print(f"I want to move {current_number_length} {current_number} to the left")
    input()

    # search leftmost group of current_number_length dots
    res = re.search(r'\.{%d}' % current_number_length, ''.join(disk))
    if res is not None:
        b, e = res.span()
        if b < right:
            disk[b:e] = current_number_length * [current_number]
            disk[right:right+current_number_length] = current_number_length * ['.']
    right -= 1


for idx, x in enumerate(disk):
    if x != '.':
        total += idx * int(x)

print(total)