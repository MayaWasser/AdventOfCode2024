input = open("input.txt", "r").readlines()
Os = ["O" for i in range(len(input[0])+1)]
grid = [Os]
for i in range(len(input)):
    row = ["O"] + list(input[i].strip()) + ["O"]
    grid.append(row)
grid.append(Os)

m = len(grid)-2
n = len(grid[0])-2

for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j] == "^":
            # guard row
            gi = i
            # guard column
            gj = j

dir = [-1,0]

count = 1
while grid[gi][gj] != "O":
    if grid[gi][gj] == ".":
        count += 1
    if grid[gi+dir[0]][gj+dir[1]] == "#":
        dir = [dir[1], -dir[0]]
    grid[gi][gj] = "X"
    gi += dir[0]
    gj += dir[1]

print(count)
