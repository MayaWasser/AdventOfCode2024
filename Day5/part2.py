input = open("input.txt", "r").readlines()
n = input.index("\n")

ord = []
for i in range(n):
    ord.append([ int(input[i].strip().split("|")[j]) for j in range(2)])


updates = []
for i in range(n+1,len(input)):
    row = input[i].strip().split(",")
    updates.append([int(row[j]) for j in range(len(row))] )

master = {}
for i in range(len(ord)):
    for j in range(2):
        p = ord[i][j]
        if p not in master:
            master[p] = [0,0]
        master[p][j] += 1


masterOrder = [0 for i in range(len(master))]
for num in master.keys():
    masterOrder[master[num][1]] += num

print(len(ord))
print(len(master))
#
# sum = 0
# for i in range(len(updates)):
#     correct = True
#     upd = updates[i]
#     for j in range(len(ord)):
#         p1 = ord[j][0]
#         p2 = ord[j][1]
#         if (p1 in upd) and (p2 in upd) and upd.index(p1) > upd.index(p2):
#             correct = False
#     if not correct:
#         MO = masterOrder.copy()
#         for j in range(len(masterOrder)):
#             if masterOrder[j] not in upd:
#                 MO.remove(masterOrder[j])
#         sum += MO[len(MO)//2]
# print(sum)
