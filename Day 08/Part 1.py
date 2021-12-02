myfile = open("Code.txt")
lines = myfile.readlines()
myfile.close()

complete = []

acc = 0

pc = 0
while pc < len(lines) -1:
    amount = 0
    for line in complete:
        if line == pc:
            amount += 1
    
    if amount < 2:
        command, data = lines[pc].strip().split(" ")
        data = int(data)
        if command == "jmp":
            pc += data
        elif command == "acc":
            acc += data
            pc += 1
        else:
            pc += 1

        complete.append(pc)
    else:
        print(acc)
        break
    
