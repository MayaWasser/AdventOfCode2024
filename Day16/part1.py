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
            maze[i][j] = "."


def solve(i,j):
    char = maze[i][j]
    if char == "E":
        printMaze()

    if char == ".":
        maze[i][j] = "@"

        up = solve(i-1,j)
        down = solve(i+1,j)
        left = solve(i,j-1)
        right = solve(i,j+1)

        # visited but not part of path
        maze[i][j] = "."


def printMaze():
    for row in maze:
        for char in row:
            print(char, end="")
        print()
    print()

solve(srow,scol)
