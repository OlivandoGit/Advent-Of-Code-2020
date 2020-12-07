myfile = open("Bags.txt")
lines = myfile.readlines()
myfile.close()

rules = {}

for line in lines:
    colour, contains = line.split(" bags contain")
    tmp = []

    parts = contains.split(" ")
    total = 0
    for i in range(len(parts)):
        if parts[i].isdigit():
            total += int(parts[i])
            tmp.append(parts[i])
            tmp.append(parts[i + 1] + " " + parts[i + 2])

    tmp.insert(0, total)

    rules[colour] = tmp

bags = ["shiny gold"]

for bag in bags:
    contains = rules[bag]

    for i in range(1, len(contains)):
        if contains[i].isdigit():
            for j in range(int(contains[i])):
                bags.append(contains[i + 1])

print(len(bags) - 1)
