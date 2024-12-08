import itertools
import os

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().splitlines()

operations = ['+', '*']
total = 0

for line in data:
    result, factors = line.split(':')
    result = int(result.strip())
    factors = [int(x.strip()) for x in factors.split(' ') if x]

    for operation in [p for p in itertools.product(operations, repeat=len(factors) - 1)]:
        current = factors[0]
        for i, factor in enumerate(factors[1:]):
            current = eval(f'{current} {operation[i]} {factor}')

        if current == result:
            total += result
            break

print(total)
