input = open("input.txt","r").readlines()
space = input.index("\n")

# parse input
input = [row.rstrip() for row in input]
grid = []
for row in input[:space]:
    new = []
    for char in row:
        if char == "@":
            new.append("@")
            new.append(".")
        elif char == "O":
            new.append("[")
            new.append("]")
        else:
            new.append(char)
            new.append(char)
    grid.append(new)

moves = "".join(input[space+1:])

m = len(grid)
n = len(grid[0])

# inital bot position
bi = -1
bj = -1

# find bot
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            grid[i][j] = "."
            bi = i
            bj = j

# helper function

def isBox(i,j,bracket,dir):
    if dir[0] == 0:
        return grid[i][j] == 
    else:
        return grid[i][j] == bracket

# (try to) solve the problem
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
    next = grid[ni][nj]

    if next == "[" or next == "]":
        # horizontal
        if dir[0] == 0:
            shift = 0
            i = ni
            j = nj
            while grid[i][j] != "#" or grid[i][j] !=

for row in grid:
    for char in row:
        print(char,end="")
    print()
