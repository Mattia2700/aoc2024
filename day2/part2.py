import os


def is_valid(nums):
    # print(nums, end=" ")
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
        # print(True)
        return True
    else:
        # print(False)
        return False


data = open(os.path.dirname(__file__) + '/input.txt', 'r').read().split('\n')

counts = 0

for line in data:
    nums = [int(x) for x in line.split(" ")]
    if is_valid(nums):
        counts += 1
    else:
        # remove each element from the list and check if the list is valid
        for idx, num in enumerate(nums):
            new_nums = nums.copy()
            new_nums.pop(idx)
            if is_valid(new_nums):
                counts += 1
                break

print(counts)
