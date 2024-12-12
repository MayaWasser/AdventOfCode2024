import math
input = open("input.txt","r").read().split()
stones = {}
for num in input:
    stones[int(num)] = 1

for i in range(6):
    new = []

    for num in stones.keys():
        if stones[num] > 0:
            if  num == 0:
                new.append(1)
            else:
                length = int(math.log10(num))+1
                pow = int( 10**(length/2) )
                if length % 2 == 0:
                    new.append(num // pow)
                    new.append(num % pow)
                else:
                    new.append(num*2024)

            stones[num] -= 1

    for k in new:
        if k not in stones:
            stones[k] = 0
        stones[k] += 1

print(stones)
total = 0
for i in stones.values():
    total += i
print(total)
