input = open("input.txt","r")
Hgrid = input.readlines()

m = len(Hgrid)
n = len(Hgrid[0])

Vgrid = []
for i in range(n):
    col = ""
    for j in range(m):
        col += Hgrid[j][i]
    Vgrid.append(col)

D1grid = []

for i in range(m):
    ud = ""
    ld = ""
    for j in range(m-i):
        ld += Hgrid[i+j][j]
        ud += Hgrid[j][i+j]
    if i != 0:
        D1grid.append(ud)
    D1grid.append(ld)

D2grid = []
for i in range(m):
    ud = ""
    ld = ""
    for j in range(i+1):
        ud += Hgrid[i-j][j]
        ld += Hgrid[m-1-j][m-1-i+j]
    if i != m:
        D2grid.append(ud)
    D2grid.append(ld)

xmas = 0
for i in range(2*m-1):
    if i < m:
        xmas += Hgrid[i].count("XMAS") + Hgrid[i][::-1].count("XMAS")\
            + Vgrid[i].count("XMAS") + Vgrid[i][::-1].count("XMAS")
    xmas += D1grid[i].count("XMAS") + D1grid[i][::-1].count("XMAS")\
        + D2grid[i].count("XMAS") + D2grid[i][::-1].count("XMAS")
print(xmas)
