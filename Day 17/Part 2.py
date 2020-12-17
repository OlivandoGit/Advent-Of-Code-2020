myfile = open("Starting.txt")
lines = myfile.readlines()
myfile.close()

active = []
size = [len(lines[0].strip()), len(lines), 0, 0]

for i in range(size[1]):
    for j in range(size[0]):
        if lines[i][j] == "#":
            active.append((j, i, 0, 0))

for i in range(6):
    print("i:", i)
    tochange = []

    for j in range(4):
        size[j] += 2

    for w in range(-(size[3] // 2), (size[3] - (size[3] // 2)) + 1):
        for z in range(-(size[2] // 2), (size[2] - (size[2] // 2)) + 1):
            for y in range(-(size[2] // 2), (size[1] - (size[2] // 2))):
                for x in range(-(size[2] // 2), (size[0] - (size[2] // 2))):  
                    current = (x, y, z, w)

                    neighbours = 0
                    for w2 in range(-1, 2):
                        for z2 in range(-1, 2):
                            for y2 in range(-1, 2):
                                for x2 in range(-1, 2):
                                    if not(x2 == 0 and y2 == 0 and z2 == 0 and w2 == 0):
                                        neighbour = (x + x2, y + y2, z + z2, w + w2)
                                        if neighbour in active:
                                            neighbours += 1

                    if current in active and neighbours not in range(2,4):
                        tochange.append(current)
                    elif current not in active and neighbours == 3:
                        tochange.append(current)

    for coord in tochange:
        if coord in active:
            active.remove(coord)
        else:
            active.append(coord)

print(len(active))
