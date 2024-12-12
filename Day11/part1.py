import math
input = open("input.txt","r").read().split()
stones = [ int(input[i]) for i in range(len(input))]

for i in range(25):
    new = []
    for num in stones:
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
    stones = new

print( len(stones) )
