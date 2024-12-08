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
    print(lst)
