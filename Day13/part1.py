import numpy as np
input = open("input.txt","r").readlines()

machines = []
for i in range(len(input)//4+1):
    new = []
    for j in range(3):
        if j == 2:
            lst = input[4*i+j].strip().split("=")
        else:
            lst = input[4*i+j].strip().split("+")
        new.append(int(lst[1].split(",")[0]))
        new.append(int(lst[2]))

    machines.append(new)


def isInt(num):
    return abs(num-round(num)) < 0.00001


tokens = 0
for claw in machines:
    # using the form Ax=b
    A = np.matrix(claw[0:4]).reshape(2,2).getT()
    b = np.matrix(claw[4:6]).reshape(2,1)
    x = np.linalg.solve(A,b)
    if isInt(x[0,0]) and isInt(x[1,0]):
        tokens += 3*x[0,0]+x[1,0]

print(tokens)
