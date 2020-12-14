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
        
        data = format(int(data), "036b")
        data = list(data)

        for i in range(len(mask)):
            if mask[i] != "X":
                data[i] = mask[i]

        data = "".join(data)
        data = int(data, 2)

        memory[int(location)] = data

total = 0
for key in memory.keys():
    total += memory[key]

print(total)