input = open("input.txt","r").readlines()
maze = [ list(input[i].rstrip()) for i in range(len(input)) ]

# starting position
srow = -1
scol = -1
scores = []

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            srow = i
            scol = j
            maze[i][j] = "."

# direction of the previous move (-1 on the first)
# 1 = up
# 2 = down
# 3 = left
# 4 = right

def solve(i,j, dir, score):
    char = maze[i][j]
    if char == "E":
        scores.append(score)
        # print(score)
        # printMaze()

    if char == ".":
        maze[i][j] = "@"

        if dir == 1:
            solve(i-1,j,1,score+1)
        else:
            solve(i-1,j,1,score+1001)

        if dir == 2:
            solve(i+1,j,2,score+1)
        else:
            solve(i+1,j,2,score+1001)

        if dir == 3:
            solve(i,j-1,3,score+1)
        else:
            solve(i,j-1,3,score+1001)

        if dir == 4:
            solve(i,j+1,4,score+1)
        else:
            solve(i,j+1,4,score+1001)


        maze[i][j] = "."


def printMaze():
    for row in maze:
        for char in row:
            print(char, end="")
        print()
    print()


solve(srow,scol, -1, 0)
print(min(scores))
