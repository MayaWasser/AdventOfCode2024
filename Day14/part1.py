input = open("input.txt","r").readlines()
bots = []

for row in input:
    bot = []
    line = row.rstrip().split()
    for j in range(2):
        bot.append([int(line[j][2:].split(",")[i]) for i in range(2)])
    bots.append(bot)

# tile height
n = 103
# tile width
m = 101

for i in range(100):
    for bot in bots:
        x = (bot[0][0] + bot[1][0]) % m
        y = (bot[0][1] + bot[1][1]) % n
        bot[0] = [x,y]

count = [0,0,0,0]
for bot in bots:
    i = bot[0][1]
    j = bot[0][0]
    if i < n//2 and j < m//2:
        count[0] += 1
    if i < n//2 and j > m//2:
        count[1] += 1
    if i > n//2 and j < m//2:
        count[2] += 1
    if i > n//2 and j > m//2:
        count[3] += 1

total = 1
for num in count:
    total *= num
print(total)

# for i in range(n):
#     for j in range(m):
#         count = 0
#         for bot in bots:
#             if bot[0][0] == j and bot[0][1] == i:
#                 count += 1
#         if count > 0:
#             print(count,end="")
#         else:
#             print(".", end="")
#     print()
