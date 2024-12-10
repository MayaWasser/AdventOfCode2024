input = open("input.txt", "r").readlines()
m = len(input)
n = len(input[0])-1

pad = [-1 for i in range(n+2)]
grid = [pad]
for i in range(m):
    row = [-1] + [int(input[i][j]) for j in range(n)] + [-1]
    grid.append(row)
grid.append(pad)

def findScore(row,col,nines):
    # current height
    h = grid[row][col]
    if  h == 9:
        nines.add((row,col))
    if grid[row+1][col] == h+1:
        findScore(row+1,col,nines)
    if grid[row][col+1] == h+1:
        findScore(row,col+1,nines)
    if grid[row-1][col] == h+1:
        findScore(row-1,col,nines)
    if grid[row][col-1] == h+1:
        findScore(row,col-1,nines)

total = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j] == 0:
            nines = set()
            findScore(i,j,nines)
            total += len(nines)
print(total)
