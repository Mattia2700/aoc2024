import os
import re

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read()

res = re.findall(r"(?:mul\((\d+?),(\d+?)\))|(?:(do)\(\))|(?:(don\'t)\(\))", data)

total = 0
count = True
for n1, n2, do, dont in res:
    if do:
        count = True
    if dont:
        count = False
    if count and n1 and n2:
        total += int(n1) * int(n2)

print(total)