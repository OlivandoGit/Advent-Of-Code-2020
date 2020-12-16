myfile = open("Tickets.txt")
lines = myfile.readlines()
myfile.close()

order = []
rules = {}

for i in range(lines.index("\n")):
    name, data = lines[i].strip().split(": ")
    data = data.split(" or ")
    
    for dat in data[:2]:
        tmp1, tmp2 = dat.split("-")
        data.append(int(tmp1))
        data.append(int(tmp2))

    del data[0]
    del data[0]

    order.append(name)
    rules[name] = data

error = 0
for i in range(lines.index("nearby tickets:\n") + 1, len(lines)):
    values = lines[i].strip().split(",")

    for value in values:
        valid = False
        for key in rules.keys():
            if int(value) in range(rules[key][0], (rules[key][1] + 1)) or int(value) in range(rules[key][2], (rules[key][3] + 1)):
                valid = True

        if not valid:
            error += int(value)

print(error)