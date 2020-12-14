myfile = open("Programme.txt")
lines = myfile.readlines()
myfile.close()

memory = {}

for line in lines:
    if line.startswith("mask"):
        mask = line[(line.index(" = ") + 2):].strip()

    else:
        location, data = line.split(" = ")

        location = "".join(filter(str.isdigit, location))
        
        location = format(int(location), "036b")
        location = list(location)

        additional = 0
        for i in range(len(mask)):
            if mask[i] == "1":
                location[i] = mask[i]
            elif mask[i] == "X":
                additional += 1

        for i in range(pow(2, additional)):
            tmp = format(i, "036b")
            tmp = list(tmp)
            
            for j in range(len(location) - 1, - 1, -1):
                if mask[j] == "X":
                    location[j] = tmp[len(tmp) - 1]
                    del tmp[len(tmp) - 1]

            memory[int("".join(location), 2)] = int(data)

total = 0
for key in memory.keys():
    total += memory[key]

print(total)