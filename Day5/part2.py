input = open("input.txt", "r").readlines()
n = input.index("\n")

ord = []
for i in range(n):
    ord.append([ int(input[i].strip().split("|")[j]) for j in range(2)])


updates = []
for i in range(n+1,len(input)):
    row = input[i].strip().split(",")
    updates.append([int(row[j]) for j in range(len(row))] )

wrong = []
for i in range(len(updates)):
    correct = True
    upd = updates[i]
    for j in range(len(ord)):
        p1 = ord[j][0]
        p2 = ord[j][1]
        if (p1 in upd) and (p2 in upd) and upd.index(p1) > upd.index(p2):
            correct = False
    if not correct:
        wrong.append(upd)

sum = 0
for i in range(len(wrong)):
    upd = wrong[i]
    master = {}
    for j in range(len(ord)):
        p1 = ord[j][0]
        p2 = ord[j][1]
        if (p1 in upd) and (p2 in upd):
            for k in range(2):
                p = ord[j][k]
                if p not in master:
                    master[p] = [0,0]
                master[p][k] += 1

    masterOrder =  [0 for n in range(len(master))]

    for num in master.keys():
        masterOrder[master[num][1]] += num

    sum += masterOrder[len(upd)//2]

print(sum)
# master = {}
# for i in range(len(ord)):
#     for j in range(2):
#         p = ord[i][j]
#         if p not in master:
#             master[p] = [0,0]
#         master[p][j] += 1
#
#
# masterOrder = [0 for i in range(len(master))]
# for num in master.keys():
#     masterOrder[master[num][1]] += num
