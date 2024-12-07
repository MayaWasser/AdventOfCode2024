from itertools import combinations

input = open("input.txt", "r").readlines()
input = [ input[i].split(" ") for i in range(len(input))]
eqs = []
for i in range(len(input)):
    eq = []
    for j in range(len(input[i])):
        num = input[i][j]
        if j == 0:
            eq.append(int(num[:len(num)-1]))
        else:
            eq.append(int(num))
    eqs.append(eq)

sum = 0
for i in range(len(eqs)):
    n = len(eqs[i])-2
    # number of +
    pos = False
    for j in range(n+1):
        for lst in combinations(range(n),j):
            total = eqs[i][1]
            for k in range(0,n):
                if k in lst:
                    total += eqs[i][k+2]
                else:
                    total *= eqs[i][k+2]
            if total == eqs[i][0]:
                sum += eqs[i][0]
                pos = True
                break
        if pos:
            break
print(sum)
