input = open("input.txt", "r").readlines()
m = len(input)
n = len(input[0])-1

pad = [-1 for i in range(n+2)]
grid = [pad]
for i in range(m):
    row = [-1] + [int(input[i][j]) for j in range(n)] + [-1]
    grid.append(row)
grid.append(pad)

def findScore(row,col, num):
    # current height
    h = grid[row][col]
    if num == 9 and h == 9:
        return 1
    if h != num:
        return 0
    return findScore(row+1,col,num+1)+findScore(row,col+1,num+1)+findScore(row-1,col,num+1)+findScore(row,col-1,num+1)

total = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        total += findScore(i,j,0)
print(total)
