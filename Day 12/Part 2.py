myfile = open("Instructions.txt")
lines = myfile.readlines()
myfile.close()

dirrections = "NESW"
waypoint = {"N":1, "E":10, "S":0, "W":0}
distances = {"N":0, "E":0, "S":0, "W":0}

for line in lines:
    if line[0] in waypoint.keys():
        waypoint[line[0]] += int(line[1:].strip())

    if line[0] == "F":
        for char in dirrections:
            distances[char] += int(line[1:].strip()) * waypoint[char]


    if line[0] == "L" or line[0] == "R":
        tmp = []
        for char in dirrections:
            tmp.append(waypoint[char])

        degrees = int(line[1:].strip()) % 360
        if line[0] == "L":
            degrees = 360 - degrees

        degrees = degrees // 90

        for i in range(len(dirrections)):
            waypoint[dirrections[(i + degrees) % 4]] = tmp[i] 

total = abs(distances["N"] - distances["S"]) + abs(distances["E"] - distances["W"])
print(total)