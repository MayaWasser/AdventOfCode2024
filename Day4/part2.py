input = open("input.txt","r")
grid = input.readlines()

m = len(grid)
n = len(grid[0])-1

Xmas = 0
for i in range(1,m-1):
    for j in range(1,n-1):
        str = ""
        if grid[i][j] == "A":
            str += grid[i+1][j+1] + grid[i-1][j-1] + grid[i+1][j-1] + grid[i-1][j+1]
        if str == "SMSM" or str == "SMMS" or str == "MSMS" or str == "MSSM":
            Xmas += 1
print(Xmas)
