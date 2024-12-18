input = open("input.txt","r").readlines()
space = input.index("\n")

input = [row.strip() for row in input]
grid = [ list(row) for row in input[:space] ]
moves = "".join(input[space+1:])

m = len(grid)
n = len(grid[0])

# inital bot position
bi = -1
bj = -1

for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            grid[i][j] = "."
            bi = i
            bj = j

def moveBoxes(i, j, dir):
    if grid[i][j] == ".":
        grid[i][j] = "O"
        return True
    elif grid[i][j] == "#":
        return False
    else:
        return moveBoxes(i+dir[0],j+dir[1],dir)

for i in range(len(moves)):
    move = moves[i]
    if move == "<":
        dir = (0,-1)
    elif move == ">":
        dir = (0,1)
    elif move == "^":
        dir = (-1,0)
    # move == "v"
    else:
        dir = (1,0)

    # new coordinates:
    ni = bi + dir[0]
    nj = bj + dir[1]

    if moveBoxes(ni, nj, dir):
        grid[ni][nj] = "."

    if grid[ni][nj]  == ".":
        bi += dir[0]
        bj += dir[1]

total = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "O":
            total += 100*i+j

print(total)

# grid[bi][bj] = "@"
# for row in grid:
#     print(row)
