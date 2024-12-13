input = open("input.txt","r").readlines()
Os = ["." for i in range(len(input[0])+1)]
grid = [Os]
for i in range(len(input)):
    row = ["."] + list(input[i].strip()) + ["."]
    grid.append(row)
grid.append(Os)

m = len(grid)-2
n = len(grid[0])-2

def findCorners(row, col, letter, sect):
    corners = 0
    grid[row][col] = sect
    # u, r, d, l
    dirs = [ [-1,0], [0,1], [1,0], [0,-1]]
    edge = [False for i in range(4)]
    # up
    for k in range(len(dirs)):
        i = row+dirs[k][0]
        j = col+dirs[k][1]
        if grid[i][j] == letter:
            corners += findCorners(i,j,letter,sect)
        elif grid[i][j] != sect:
            edge[k] = True

    # ul corner
    if edge[0] and edge[3]:
        corners += 1
    # ur corner
    if edge[0] and edge[1]:
        corners += 1
    # dr corner
    if edge[2] and edge[1]:
        corners += 1
    # dl corner
    if edge[2] and edge[3]:
        corners += 1
    return corners

print(findCorners(2,3,"C","1"))
for row in grid:
    print(row)
# # returns (area, perimeter)
# def findAP(row,col,letter,sect):
#     if grid[row][col] == sect:
#         return (0,0)
#     if grid[row][col] != letter:
#         return (0,1)
#     else:
#         grid[row][col] = sect
#         l= findAP(row,col-1,letter,sect)
#         r = findAP(row,col+1,letter,sect)
#         u = findAP(row+1,col,letter,sect)
#         d = findAP(row-1,col,letter,sect)
#         return (l[0]+r[0]+u[0]+d[0]+1, l[1]+r[1]+u[1]+d[1])
#
# price = 0
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         if grid[i][j].isalpha():
#             a,p = findAP(i,j,grid[i][j],str(sect))
#             price += a*p
#             sect += 1
#
# print(price)
