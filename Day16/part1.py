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


def solve(i, j):
    char = maze[i][j]
    if char == "#" or char == "@" or char == "*":
        return -1
    if char == "E":
        return 0

    maze[i][j] = "@"
    up = solve(i-1,j)
    if up != -1:
        return 1+up

    down = solve(i+1,j)
    if down != -1 :
        return 1+down

    left = solve(i,j-1)
    if left != -1 :
        return 1+left

    right = solve(i,j+1)
    if right != -1 :
        return 1+right

    # visited but not part of path
    maze[i][j] = "*"
    
    return -1

solve(srow,scol)

for row in maze:
    for char in row:
        print(char, end="")
    print()
