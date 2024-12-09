input = open("input.txt", "r").readlines()[0].strip()

disk = []
index = 0
for i in range(len(input)):
    if i%2==0:
        disk.append([i//2,index,int(input[i])])
    index += int(input[i])

i = len(disk)-1
while i > 0:
    moved = False
    for j in range(0, i):
        if disk[j+1][1] - (disk[j][1]+disk[j][2]) >= disk[i][2]:
            disk[i][1] = disk[j][1]+disk[j][2]
            disk.insert(j+1, disk.pop(i))
            moved = True
            break
    if not moved:
        i -= 1

checksum = 0
index = 0
for i in range(len(disk)):
    index = disk[i][1]
    for j in range(disk[i][2]):
        checksum += disk[i][0] * index
        index += 1
        
print(checksum)
