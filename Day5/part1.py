input = open("input.txt", "r").readlines()
n = input.index("\n")

ord = []
for i in range(n):
    ord.append([ int(input[i].strip().split("|")[j]) for j in range(2)])


updates = []
for i in range(n+1,len(input)):
    row = input[i].strip().split(",")
    updates.append([int(row[j]) for j in range(len(row))] )

sum = 0
for i in range(len(updates)):
    correct = True
    upd = updates[i]
    for j in range(len(ord)):
        p1 = ord[j][0]
        p2 = ord[j][1]
        if (p1 in upd) and (p2 in upd) and upd.index(p1) > upd.index(p2):
            correct = False
    if correct:
        sum += upd[ len(upd)//2 ]

print(sum)
