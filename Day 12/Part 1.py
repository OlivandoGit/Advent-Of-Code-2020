myfile = open("Instructions.txt")
lines = myfile.readlines()
myfile.close()

facing = 90
dirrections = "NESW"
distances = {"N":0, "E":0, "S":0, "W":0}

for line in lines:
    if line[0] in distances.keys():
        distances[line[0]] += int(line[1:].strip())

    if line[0] == "F":
        distances[dirrections[(facing // 90)]] += int(line[1:].strip())

    if line[0] == "L":
        facing -= int(line[1:].strip())
    if line[0] == "R":
        facing += int(line[1:].strip())

    facing = facing % 360 


print(distances)

total = abs(distances["N"] - distances["S"]) + abs(distances["E"] - distances["W"])
print(total)