myfile = open("Code.txt")
lines = myfile.readlines()
myfile.close()

complete = []

acc = 0
last = 0
pc = 0
while pc < len(lines):
    amount = 0
    for line in complete:
        if line == pc:
            amount += 1
    
    if amount < 2:
        command, data = lines[pc].strip().split(" ")

        data = int(data)
        if command == "jmp":
            last = pc
            pc += data
        elif command == "acc":
            acc += data
            pc += 1
        else:
            lat = pc
            pc += 1

        complete.append(pc)
    else:
        command, data = lines[last].strip().split(" ")
        if command == "jmp":
            lines[last] = "nop " + data
        else:
            lines[last]= "jmp " + data
        
        pc = 0
        acc = 0
        last = 0
        complete = []

print(acc)
