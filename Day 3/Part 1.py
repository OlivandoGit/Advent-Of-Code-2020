myfile = open("slope.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


amounts = []


vpos = 0
hpos = 0
amount = 0
hdelta = 3
vdelta = 1

while vpos < len(lines) - 1:
    vpos += vdelta
    if vpos > len(lines) - 1:
        vpos = len(lines) - 1

    hpos = (hpos + hdelta) % len(lines[i])

    if lines[vpos][hpos] == "#":
        amount += 1

amounts.append(amount)

total = 1
for amt in amounts:
    total *= amt

print(total)