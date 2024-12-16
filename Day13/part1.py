# import numpy as np
# input = open("input.txt","r").readlines()
#
# machines = []
# for i in range(len(input)//4+1):
#     new = []
#     for j in range(3):
#         if j == 2:
#             lst = input[4*i+j].strip().split("=")
#         else:
#             lst = input[4*i+j].strip().split("+")
#         new.append(int(lst[1].split(",")[0]))
#         new.append(int(lst[2]))
#
#     machines.append(new)
#
#
# def isInt(num):
#     return abs(int(num)-num) < 0.0001
#
# tokens = 0
# for claw in machines:
#     # using the form Ax=b
#     A = np.matrix(claw[0:4]).reshape(2,2).getT()
#     b = np.matrix(claw[4:6]).reshape(2,1)
#     x = np.linalg.solve(A,b)
#     if isInt(x[0,0]) and isInt(x[1,0]):
#         tokens += int(3*x[0,0]+x[1,0])
#
# print(tokens)

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def solve(part: int):
    tokens = 0
    add = 10000000000000 if part == 2 else 0
    for line in lines:
        if line.startswith("Button"):
            l = line.split(" ")
            a = l[1].split(":")[0]
            if a == 'A':
                x1 = int(l[2][2:-1])
                y1 = int(l[3][2:])
            else:
                x2 = int(l[2][2:-1])
                y2 = int(l[3][2:])

        elif line.startswith("Prize"):
            l = line.split(" ")
            c = int(l[1][2:-1]) + add
            d = int(l[2][2:]) + add
            a = (c*y2 - d*x2) / (x1*y2 - y1*x2)
            b = (d*x1 - c*y1) / (x1*y2 - y1*x2)
            if a == int(a) and b == int(b):
                tokens += int(3 * a + b)

    print(tokens)

solve(1)
solve(2)
