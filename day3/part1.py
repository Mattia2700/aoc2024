import os
import re

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read()

res = re.findall(r'mul\((\d+?),(\d+?)\)', data)
total = 0
for a, b in res:
    total += int(a) * int(b)

print(total)