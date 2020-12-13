myfile = open("Busses.txt")
lines = myfile.readlines()
myfile.close()

times = lines[1].strip().split(",")

highest = 0

for i in range(len(times)):
    if times[i] != "x":
        times[i] = int(times[i])

current = 0
delta = 1
first = -1

time = 0
found = False
while not found:
    time += delta

    if (time + current) % times[current] == 0:
        if first == -1:
            first = time

            if current == len(times) - 1:
                found = True

        else:
            delta = time - first
            first = -1
            current += 1

            while current < len(times) and times[current] == "x":
                current += 1  


print(time)