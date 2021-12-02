myfile = open("Expenses.txt")

lines = myfile.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for line in lines:
    for l in lines:
        if int(line) + int(l) == 2020:
            print(int(line)*int(l))

myfile.close()