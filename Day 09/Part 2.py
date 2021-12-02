myfile = open("List.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

length = 25

for i in range(length + 1, len(lines)):
    subsect = lines[(i - length):i]
    
    valid = False
    for num in subsect:       
        for num2 in subsect:
            if num + num2 == lines[i] and num != num2:
                valid = True

    if not valid:
        invalid = lines[i]
        break

for i in range(len(lines)):
    tmp = invalid
    for j in range(i, len(lines)):
        tmp -= lines[j]
        
        if tmp == 0:
            subset = lines[i:j + 1]
            subset.sort()
            print(subset[0] + subset[len(subset) - 1])
        