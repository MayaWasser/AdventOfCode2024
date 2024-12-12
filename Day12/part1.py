input = open("input.txt","r").readlines()
Os = ["." for i in range(len(input[0])+1)]
grid = [Os]
for i in range(len(input)):
    row = ["."] + list(input[i].strip()) + ["."]
    grid.append(row)
grid.append(Os)

m = len(grid)-2
m = len(grid[0])-2

# # Find area and perimeter of a section, returns (area, perimeter)
# def findAP (row, col, letter, sect):
#     entry = grid[row][col]
#     if entry == letter:
#         grid[row][col] = sect
#         left = findAP(row,col-1,letter,sect)
#         right = findAP(row,col+1,letter,sect)
#         up = findAP(row-1,col+1,letter,sect)
#         down = findAP(row+1,col,letter,sect)
#         area = left[0]+right[0]+up[0]+down[0]
#         per = left[1]+right[1]+up[1]+down[1]
#         return (area+1,per)
#     if entry == sect:
#         return (0,0)
#     else:
#         return (0,1)

def findArea(row,col,letter,sect):
    if grid[row][col] != letter:
        return 0
    else:
        grid[row][col] = sect
        return findArea(row+1,col,letter,sect)+findArea(row-1,col,letter,sect)+findArea(row,col+1,letter,sect)+findArea(row,col-1,letter,sect)+1

def findPerimeter(row,col,letter,sect):
    if grid[row][col] == sect:
        return 0
    if grid[row][col] != letter :
        return 1
    else:
        grid[row][col] = sect
        return findPerimeter(row+1,col,letter,sect)+findPerimeter(row-1,col,letter,sect)+findPerimeter(row,col+1,letter,sect)+findPerimeter(row,col-1,letter,sect)


for i in grid:
    print(i)
