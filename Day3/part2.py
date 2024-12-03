input = open("input.txt","r").read()

sum = 0
mult = True
while input != "":
    i = input.find("mul(")

    do = input[:i].find("do()")
    dont = input[:i].find("don't()")
    if do != -1 or dont != -1:
        if do < dont:
            mult = False
        else:
            mult = True

    closing = input[i:].find(")")+i
    if closing != -1:
        cmnd = input[i+4:closing]
        nums = cmnd.partition(",")
        if nums[0].isdigit() and nums[2].isdigit():
            if mult:
                sum += int(nums[0])*int(nums[2])
            input = input[closing+1:]
        else:
            input = input[i+4:]
    else:
        input = ""
print(sum)
