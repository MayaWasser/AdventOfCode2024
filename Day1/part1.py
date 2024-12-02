import numpy as np
input = open("input.txt","r")
lines = input.readlines()

left = []
right = []
for i in range(len(lines)):
    nums = lines[i].split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))

sum = 0

for i in range(len(left)):
    lmin = np.argmin(left)
    rmin = np.argmin(right)
    sum += abs(left.pop(lmin)-right.pop(rmin))

print(sum)
