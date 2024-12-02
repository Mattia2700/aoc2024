import os

data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().split('\n')

counts = 0

for line in data:
    nums = [int(x) for x in line.split(" ")]
    increasing, decreasing, valid = False, False, True
    for idx, num in enumerate(nums):
        if idx == 0:
            continue
        else:
            if nums[idx] > nums[idx - 1]:
                increasing = True
            elif nums[idx] < nums[idx - 1]:
                decreasing = True

            if abs(nums[idx] - nums[idx - 1]) < 1 or abs(nums[idx] - nums[idx - 1]) > 3:
                valid = False
                break

    if (increasing != decreasing) and valid:
        counts += 1

print(counts)
