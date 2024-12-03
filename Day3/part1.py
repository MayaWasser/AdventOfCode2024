input = open("input.txt","r").read()

sum = 0
while input != "":
    i = input.find("mul(")
    closing = input[i:].find(")")+i
    if closing != -1:
        cmnd = input[i+4:closing]
        nums = cmnd.partition(",")
        if nums[0].isdigit() and nums[2].isdigit():
            sum += int(nums[0])*int(nums[2])
            input = input[closing+1:]
        else:
            input = input[i+4:]
    else:
        input = ""
print(sum)
