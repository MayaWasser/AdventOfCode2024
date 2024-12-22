input = open("input.txt","r").readlines()
maze = [ list(input[i].rstrip()) for i in range(len(input)) ]

# starting position
srow = -1
scol = -1

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            srow = i
            scol = j


# direction of previous move
# -1 on the first move
# up = 1
# down = 2
# left = 3
# right = 4

def solve(i, j, dir,score,lst):
    char = maze[i][j]
    if char == "#" or char == "@" or char == "*":
        return -1
    if char == "E":
        lst.append(score)
        print(score)
        score = 0
        return 0

    maze[i][j] = "@"
    up = solve(i-1,j,1,score,lst)
    if up != -1:
        if dir == 1 or dir == -1:
            score += 1
        else:
            score += 1000

    down = solve(i+1,j,2,score,lst)
    if down != -1 :
        if dir == 2  or dir == -1:
            score += 1
        else:
            score += 1000

    left = solve(i,j-1,3,score,lst)
    if left != -1 :
        if dir == 3  or dir == -1:
            score += 1
        else:
            score += 1000

    right = solve(i,j+1,4,score,lst)
    if right != -1 :
        if dir == 4  or dir == -1:
            score += 1
        else:
            score += 1000

    # visited but not part of path
    maze[i][j] = "*"

    return -1

lst = []
score = 0
dir = -1
print( solve(srow,scol,dir,score,lst) )
print(lst)

for row in maze:
    for char in row:
        print(char, end="")
    print()
