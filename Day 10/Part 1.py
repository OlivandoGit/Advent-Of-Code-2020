myfile = open("Adapters.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

lines.sort()
lines.insert(0, 0)
lines.append(lines[len(lines) - 1] + 3)

diff1 = 0
diff3 = 0

for i in range(len(lines) - 1):
    if lines[i] == lines[i + 1] - 1:
        diff1 += 1
    elif lines[i] == lines[i + 1] - 3:
        diff3 += 1

print(diff1)
print(diff3)

print (diff1 * diff3)