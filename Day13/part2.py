import numpy as np
input = open("input.txt","r").readlines()

machines = []
for i in range(len(input)//4+1):
    new = []
    for j in range(3):
        if j == 2:
            lst = input[4*i+j].strip().split("=")
            new.append(int(lst[1].split(",")[0])+10000000000000)
            new.append(int(lst[2])+10000000000000)
        else:
            lst = input[4*i+j].strip().split("+")
            new.append(int(lst[1].split(",")[0]))
            new.append(int(lst[2]))

    machines.append(new)

def isInt(num):
    return abs(num-round(num)) < 0.00001


tokens = 0
for claw in machines:
    ax = claw[0]
    ay = claw[1]
    bx = claw[2]
    by = claw[3]
    x0 = claw[4]
    y0 = claw[5]
    aPress, aRem = divmod(x0*by-bx*y0, ax*by-bx*ay)
    if aRem == 0:
        bPress, bRem = divmod(y0*ax-ay*x0, ax*by-bx*ay)
        if bRem == 0:
            tokens += 3*aPress+bPress

print(tokens)
