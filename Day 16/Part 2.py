myfile = open("Tickets.txt")
lines = myfile.readlines()
myfile.close()

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

    rules[name] = data

tickets = []
for i in range(lines.index("nearby tickets:\n") + 1, len(lines)):
    values = lines[i].strip().split(",")

    fieldsvalid = 0
    for value in values:
        valid = False
        for key in rules.keys():
            if int(value) in range(rules[key][0], (rules[key][1] + 1)) or int(value) in range(rules[key][2], (rules[key][3] + 1)):
                valid = True

        if valid:
            fieldsvalid += 1

    if fieldsvalid == len(rules):
        tickets.append(values)

order = []
fields = [[] for i in range(len(tickets[0]))]

for ticket in tickets:
    for i in range(len(ticket)):
        fields[i].append(ticket[i])

for field in fields:
    tmp = []
    for key in rules.keys():
        valid = True

        for value in field:
            if int(value) not in range(rules[key][0], (rules[key][1] + 1)) and int(value) not in range(rules[key][2], (rules[key][3] + 1)):
                valid = False

        if valid:
            tmp.append(key)

    order.append(tmp)

changed = True
while changed:
    changed = False

    for i in range(len(order)):
        if len(order[i]) == 1:
            for j in range(len(order)):
                if order[i][0] in order[j] and j != i:
                    order[j].remove(order[i][0])
                    changed = True

myticket = lines[lines.index("your ticket:\n") + 1].strip().split(",")

total = 1 
for i in range(len(order)):
    if order[i][0].startswith("departure"):
        total *= int(myticket[i])

print(total)