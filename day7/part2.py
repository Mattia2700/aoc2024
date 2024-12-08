import itertools
import os

from tqdm import tqdm

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().splitlines()

operations = ['+', '*', '||']
total = 0

for line in tqdm(data):
    result, factors = line.split(':')
    result = int(result.strip())
    factors = [int(x.strip()) for x in factors.split(' ') if x]

    for operation in tqdm([p for p in itertools.product(operations, repeat=len(factors) - 1)], leave=False):
        current = factors[0]

        for i, factor in enumerate(factors[1:]):
            if operation[i] == '||':
                current = int(str(current) + str(factor))
            else:
                current = eval(f'{current} {operation[i]} {factor}')

        if current == result:
            total += result
            break

print(total)
