myfile = open("Answers.txt")
lines = myfile.readlines()
myfile.close()

groups = []

pointer = 0
for i in range(len(lines)):
    if lines[i].strip() == "" or i == len(lines) - 1:
        group = ""
        for j in range(pointer, i + 1):
            group += lines[j].strip()

        groups.append(group)
        pointer = i + 1

for i in range(len(groups)):
    chars = ""
    for char in groups[i]:
        if char not in chars:
            chars += char

    groups[i] = chars

total = 0
for group in groups:
    total += len(group)
    
print(total)