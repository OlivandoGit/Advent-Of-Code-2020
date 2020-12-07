myfile = open("Expenses.txt")

lines = myfile.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for line in lines:
    for lin in lines:
        ans1 = int(line) + int(lin)
        if ans1 < 2020:
            for l in lines:
                if ans1 + int(l) == 2020:
                    print(int(line) * int(lin) * int(l))


myfile.close()