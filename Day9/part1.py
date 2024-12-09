input = open("input.txt", "r").readlines()[0].strip()

disk = []
for i in range(len(input)):
    if i%2==0:
        num = i//2
    else:
        num = -1
    for j in range(int(input[i])):
        disk.append(num)

i = 0
while i < len(disk)-1:
    if disk[i] == -1:
        j = len(disk)-1
        while disk[j] == -1:
            disk.pop(j)
            j -= 1
        disk[i] = disk.pop(j)
    i += 1

checksum = 0
j = 0
while j!=-1 and j < len(disk):
    checksum += j*disk[j]
    j += 1
print(checksum)
