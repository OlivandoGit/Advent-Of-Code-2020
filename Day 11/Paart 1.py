myfile = open("Map.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = list(lines[i].strip())

changed = True

while changed:
    changed = False
    tochange = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):

            occupied = 0

            for y in range(-1, 2):
                if i + y >= 0 and i + y <= (len(lines) - 1):
                    for x in range(-1, 2):
                        if j + x >= 0 and j + x <= (len(lines[0]) - 1):
                            if not(x == 0 and y == 0):
                                if lines[i + y][j + x] == "#":
                                    occupied += 1

            if lines[i][j] == "L" and occupied == 0:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                tmp.append("#")
                tochange.append(tmp)
                changed = True
            elif lines[i][j] == "#" and occupied >= 4:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                tmp.append("L")
                tochange.append(tmp)
                changed = True

    for item in tochange:
        lines[item[0]][item[1]] = item[2]

total = 0
for line in lines:
    for char in line:
        if char == "#":
            total += 1

print(total)