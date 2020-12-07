myfile = open("Answers.txt")
lines = myfile.readlines()
myfile.close()

groups = []

pointer = 0
for i in range(len(lines)):
    if lines[i].strip() == "" or i == len(lines) - 1:
        group = []
        for j in range(pointer, i + 1):
            group.append(lines[j].strip())

        groups.append(group)
        pointer = i + 1

total = 0
for group in groups:
    print(group)
    for char in group[0]:
        add = True
        for person in group:
            if char not in person and person != "":
                add = False

        if add:
            total += 1
            
print(total)
