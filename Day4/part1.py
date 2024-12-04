input = open("input.txt","r")
grid = input.readlines()

xmas = 0

letters = {0:"X",1:"M",2:"A",3:"S"}
def findXmas (row, col, letter):
    if row < 0 or col < 0  or row >= len(grid) or col >= len(grid[0]):
        return 0

    if letter < 3 and grid[row][col] == letters[letter]:
        return findXmas(row+1,col, letter+1) + \
           findXmas(row-1,col, letter+1) + \
           findXmas(row,col+1, letter+1) + \
           findXmas(row,col-1, letter+1) + \
           findXmas(row+1,col+1, letter+1) +\
           findXmas(row-1,col-1, letter+1) +\
           findXmas(row+1,col-1, letter+1) +\
           findXmas(row-1,col+1, letter+1)
    elif letter == 3 and grid[row][col] == "S":
        return 1
    else:
        return 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        xmas += findXmas(i,j,0)
print(xmas)
