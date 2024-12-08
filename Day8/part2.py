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
        i,j = comb[0]
        while i >= 0 and i < m and j >=0 and j < m:
            anodes[i][j] = "#"
            i = i+di
            j = j+dj
        i,j = comb[1]
        while i >= 0 and i < m and j >=0 and j < m:
            anodes[i][j] = "#"
            i = i-di
            j = j-dj
            
count = 0
for row in anodes:
    for char in row:
        if char == "#":
            count+=1
print(count)
