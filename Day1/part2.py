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
    count = right.count(left[i])
    sum += count * left[i]

print(sum)
