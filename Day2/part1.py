input = open("input.txt", "r")
lines = input.readlines()

reports = []
for i in range(len(lines)):
    level = lines[i].split()
    reports.append([int(level[i]) for i in range(len(level))])

safe = 0
for i in range(len(reports)):
    level = reports[i]
    isSafe = True
    increasing = level[0] < level[1]
    for j in range(len(level)-1):
        isSafe = isSafe and abs(level[j+1]-level[j]) <=3
        if isSafe:
            if increasing:
                isSafe = level[j] < level[j+1]
            else:
                isSafe = level[j] > level[j+1]
    if isSafe:
        safe +=1

print(safe)
