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
            initi = i
            # guard column
            initj = j

count = 0
for i in range(1,m+1):
    for j in range(1,n+2):
        if grid[i][j] == ".":
            # test grid
            test = grid.copy()
            test[i][j] = "#"
            # guard coordinates and direction
            gi = initi-1
            gj = initj
            dir = [-1,0]
            while test[gi][gj]!= "O" or (gi==initi and gj ==initj and dir==[-1,0]):
                if test[gi+dir[0]][gj+dir[1]] == "#":
                    dir = [dir[1], -dir[0]]
                test[gi][gj] = "X"
                gi += dir[0]
                gj += dir[1]
            if test[gi][gj] != "O":
                count += 1
            for k in range(len(test)):
                print(test[k])
            print("-------------------------------")
print(count)
