import copy
input = open("input.txt","r").readlines()
Os = ["." for i in range(len(input[0])+1)]
grid = [Os]
for i in range(len(input)):
    row = ["."] + list(input[i].strip()) + ["."]
    grid.append(row)
grid.append(Os)
grid2 = copy.deepcopy(grid)

m = len(grid)-2
n = len(grid[0])-2

def findCorners(row, col, letter, sect):
    corners = 0
    grid[row][col] = sect
    # u, r, d, l and diagonals (ur, ul, dl, dr)
    dirs = [ [-1,0], [0,1], [1,0], [0,-1], [-1,1], [-1,-1],[1,-1], [1,1]]
    edge = [False for i in range(8)]
    # up
    for k in range(len(dirs)):
        i = row+dirs[k][0]
        j = col+dirs[k][1]
        if grid[i][j] == letter and k < 4:
            corners += findCorners(i,j,letter,sect)
        if grid[i][j] != sect and grid[i][j] != letter:
            edge[k] = True

    # ul corner
    if edge[0] and edge[3]:
        corners += 1
        # print("1")
    # ur corner
    if edge[0] and edge[1]:
        corners += 1
        # print("2")
    # dr corner
    if edge[2] and edge[1]:
        corners += 1
        # print("3")
    # dl corner
    if edge[2] and edge[3]:
        corners += 1
        # print("4")
    # ur inner corner
    if (not edge[0]) and (not edge[1]) and edge[4]:
        corners += 1
        # print("5")
    # ul inner corner
    if (not edge[0]) and (not edge[3]) and edge[5]:
        corners += 1
        # print("6")
    # dl inner corner
    if (not edge[2]) and (not edge[3]) and edge[6]:
        corners += 1
        # print("7")
    # dr inner corner
    if (not edge[2]) and (not edge[1]) and edge[7]:
        corners += 1
        # print("8")

    return corners

def findArea(row,col,letter,sect):
    if grid2[row][col] != letter:
        return 0
    else:
        grid2[row][col] = sect
        return findArea(row+1,col,letter,sect)+findArea(row-1,col,letter,sect)+findArea(row,col+1,letter,sect)+findArea(row,col-1,letter,sect)+1

price = 0
sect = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j].isalpha():
            # print(i,j, grid[i][j], str(sect))
            a = findArea(i,j,grid[i][j],str(sect))
            p = findCorners(i,j,grid[i][j], str(sect))
            price += a*p
            sect += 1

# for row in grid:
#     print(row)

print(price)
