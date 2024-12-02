input = open("input.txt", "r")
lines = input.readlines()

reports = []
for i in range(len(lines)):
    level = lines[i].split()
    reports.append([int(level[i]) for i in range(len(level))])

def isLevelSafe(level):
    isSafe = True
    increasing = level[0] < level[1]
    for j in range(len(level)-1):
        isSafe = isSafe and abs(level[j+1]-level[j]) <=3
        if isSafe:
            if increasing:
                isSafe = level[j] < level[j+1]
            else:
                isSafe = level[j] > level[j+1]
    return isSafe

safe = 0
for i in range(len(reports)):
    lev = reports[i]
    levSafe = False
    for j in range(len(lev)):
        levCopy = lev.copy()
        levCopy.pop(j)
        levSafe = levSafe or isLevelSafe(levCopy)
    if levSafe:
        safe += 1

print(safe)
