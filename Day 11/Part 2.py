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

            ##LEFT
            x = j - 1
            while x >= 0:
                if lines[i][x] == "#" or lines[i][x] == "L":
                    if lines[i][x] == "#":
                        occupied += 1
                    x = -1
                else:
                    x -= 1

            ##RIGHT
            x = j + 1
            while x <= len(lines[0]) - 1:
                if lines[i][x] == "#" or lines[i][x] == "L":
                    if lines[i][x] == "#":
                        occupied += 1
                    x = len(lines[0])
                else:
                    x += 1

            ##UP
            y = i - 1
            while y >= 0:
                if lines[y][j] == "#" or lines[y][j] == "L":
                    if lines[y][j] == "#":
                        occupied += 1
                    y = -1
                else:
                    y -= 1

            ##DOWN
            y = i + 1
            while y <= len(lines) - 1:
                if lines[y][j] == "#" or lines[y][j] == "L":
                    if lines[y][j] == "#":
                        occupied += 1
                    y = len(lines)
                else:
                    y += 1

            ##UP-LEFT
            x = j - 1
            y = i - 1
            while x >= 0 and y >= 0:
                if lines[y][x] == "#" or lines[y][x] == "L":
                    if lines[y][x] == "#":
                        occupied += 1
                    x = -1

                else:
                    x -= 1
                    y -= 1

            ##UP-RIGHT
            x = j + 1
            y = i - 1
            while x <= (len(lines[0]) - 1) and y >= 0:
                if lines[y][x] == "#" or lines[y][x] == "L":
                    if lines[y][x] == "#":
                        occupied += 1
                    y = -1

                else:
                    x += 1
                    y -= 1

            ##DOWN-LEFT
            x = j - 1
            y = i + 1
            while x >= 0 and y <= (len(lines) - 1):
                if lines[y][x] == "#" or lines[y][x] == "L":
                    if lines[y][x] == "#":
                        occupied += 1
                    x = -1

                else:
                    x -= 1
                    y += 1

            ##DOWN-RIGHT
            x = j + 1
            y = i + 1
            while x <= (len(lines[0]) - 1) and y <= (len(lines) - 1):
                if lines[y][x] == "#" or lines[y][x] == "L":
                    if lines[y][x] == "#":
                        occupied += 1
                    x = len(lines[0])

                else:
                    x += 1
                    y += 1

            if lines[i][j] == "L" and occupied == 0:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                tmp.append("#")
                tochange.append(tmp)
                changed = True
            elif lines[i][j] == "#" and occupied >= 5:
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