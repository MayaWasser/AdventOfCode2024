import copy
input = open("input.txt", "r").readlines()
Os = ["O" for i in range(len(input[0])+1)]
grid = [Os]
for i in range(len(input)):
    row = ["O"] + list(input[i].strip()) + ["O"]
    grid.append(row)
grid.append(Os)

m = len(grid)-2
n = len(grid[0])-2

for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j] == "^":
            # guard row
            initi = i
            # guard column
            initj = j

count = 0
for i in range(1,m+1):
    for j in range(1,n+2):
        if grid[i][j] == ".":
            # test grid
            test = copy.deepcopy(grid)
            test[i][j] = "#"
            # guard coordinates and direction
            gi = initi
            gj = initj
            dir = [-1,0]
            step = 0
            while test[gi][gj]!= "O" and not(gi==initi and gj==initj and dir==[-1,0] and step!=0):
                if test[gi+dir[0]][gj+dir[1]] == "#":
                    dir = [dir[1], -dir[0]]
                test[gi][gj] = "X"
                gi += dir[0]
                gj += dir[1]
                step += 1
            if test[gi][gj] != "O":
                count += 1

print(count)
# for i in range(len(grid)):
#     print(grid[i])

# with open("input.txt") as f:
#   rows = [line.strip() for line in f.read().strip().split("\n")]
#
# width, height = len(rows[0]), len(rows)
# sx, sy = next((x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c in "<>v^")
#
# directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# direction_map = {
#   ">": (1, 0),
#   "<": (-1, 0),
#   "^": (0, -1),
#   "v": (0, 1)
# }
#
# def get_jump_location(x, y, dindex):
#   if rows[y][x] == "#":
#     return None
#
#   dx, dy = directions[dindex]
#   while x >= 0 and y >= 0 and x < width and y < height and rows[y][x] != "#":
#     x += dx
#     y += dy
#
#   if x < 0 or y < 0 or x >= width or y >= height:
#     return (x, y, None)
#
#   x -= dx
#   y -= dy
#   dindex = (dindex + 1) % 4
#   return (x, y, dindex)
#
# jump_map = {(x, y, di): get_jump_location(x, y, di) for x in range(width) for y in range(height) for di in range(len(directions))}
#
# def jump_into_block(dindex, block_patch):
#   dx, dy = directions[dindex]
#   bx, by = block_patch
#   return (bx - dx, by - dy, (dindex + 1) % 4)
#
# def jump(x, y, dindex, block_patch):
#   dest = jump_map[x, y, dindex]
#   if block_patch is not None and dest is not None:
#     fx, fy, _ = dest
#     bx, by = block_patch
#     if fx == bx and min(y, fy) <= by <= max(y, fy):
#       return jump_into_block(dindex, block_patch)
#     elif min(x, fx) <= bx <= max(x, fx) and fy == by:
#       return jump_into_block(dindex, block_patch)
#   return dest
#
#
# def get_full_path():
#   x, y = sx, sy
#
#   visited = set()
#   dindex = directions.index(direction_map[rows[y][x]])
#
#   step = 0
#   while True:
#     visited.add((x, y))
#
#     dx, dy = directions[dindex]
#     x, y = x + dx, y + dy
#     step += 1
#     if x < 0 or y < 0 or x >= width or y >= height:
#       break
#     elif rows[y][x] == "#":
#       x, y = x - dx, y - dy
#       dindex = (dindex + 1) % len(directions)
#
#   return visited
#
# def path_loops_with_patch(block_patch):
#   x, y = sx, sy,
#   dindex = directions.index(direction_map[rows[y][x]])
#
#   visited = set()
#
#   while True:
#     x, y, dindex = jump(x, y, dindex, block_patch)
#     if dindex is None:
#       return False
#
#     if (x, y, dindex) in visited:
#       return True
#
#     visited.add((x, y, dindex))
#
# path = get_full_path()
# print(len(path))
#
# loop_positions = 0
# for block in path:
#   if block != (sx, sy) and path_loops_with_patch(block):
#     loop_positions += 1
#
# print(loop_positions)
