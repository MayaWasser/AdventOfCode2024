input = open("input.txt", "r").readlines()
n = input.index("\n")

ord = []
for i in range(n):
    ord.append([ int(input[i].strip().split("|")[j]) for j in range(2)])


updates = []
for i in range(n+1,len(input)):
    row = input[i].strip().split(",")
    updates.append([int(row[j]) for j in range(len(row))] )


def isRight(row):
    correct = True
    for j in range(len(ord)):
        p1 = ord[j][0]
        p2 = ord[j][1]
        if (p1 in row) and (p2 in row) and row.index(p1) > row.index(p2):
            correct = False
    return correct

def swap(row,m,n):
    temp = row[m]
    row[m] = row[n]
    row[n] = temp

sum = 0
for i in range(len(updates)):
    upd = updates[i]
    k = 0
    while not isRight(upd):
        k += 1
        for j in range(len(row)):
            p1 = ord[j][0]
            p2 = ord[j][1]
            if (p1 in row) and (p2 in row) and row.index(p1) > row.index(p2):
                swap(upd, row.index(p1), row.index(p2))
    if k > 0:
        sum += upd[len(upd)//2]
print(sum)
# wrong = []
# for i in range(len(updates)):
#     correct = True
#     upd = updates[i]
#     for j in range(len(ord)):
#         p1 = ord[j][0]
#         p2 = ord[j][1]
#         if (p1 in upd) and (p2 in upd) and upd.index(p1) > upd.index(p2):
#             correct = False
#     if not correct:
#         wrong.append(upd)
