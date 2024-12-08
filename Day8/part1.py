from itertools import combinations
input = open("input.txt","r").readlines()
m = len(input)
n = len(input[0])-1

anodes = [["." for i in range(n)] for j in range(m) ]
freqs = {}
for i in range(m):
    for j in range(n):
        char = input[i][j]
        if char != ".":
            if char not in freqs:
                freqs[char] = []
            freqs[char].append((i,j))

for lst in freqs.values():
    for comb in combinations(lst,2):
        di = comb[0][0]-comb[1][0]
        dj = comb[0][1]-comb[1][1]
        i1 = comb[0][0]+di
        i2 = comb[1][0]-di
        j1 = comb[0][1]+dj
        j2 = comb[1][1]-dj
        if i1 >= 0 and i1 < m and j1 >= 0  and j1 < n:
            anodes[i1][j1] = "#"
        if i2 >= 0 and i2 < m and j2 >= 0  and j2 < n:
            anodes[i2][j2] = "#"

count = 0
for row in anodes:
    for char in row:
        if char == "#":
            count+=1
print(count)
