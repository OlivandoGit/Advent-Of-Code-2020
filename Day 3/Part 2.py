myfile = open("slope.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


amounts = []

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slope in slopes:
    vpos = 0
    hpos = 0
    amount = 0
    hdelta, vdelta = tuple(slope)

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