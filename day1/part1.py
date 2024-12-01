import os

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().split('\n')

left = []
right = []

for line in data:
    values = [int(x) for x in line.split(' ') if x]
    left.append(values[0])
    right.append(values[1])

left = sorted(left)
right = sorted(right)

differences = [abs(left[i] - right[i]) for i in range(len(left))]

print(sum(differences))
