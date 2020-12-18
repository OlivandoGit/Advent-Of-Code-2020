def completemaths(expression):
    total = 0
    symbol = None
    for char in expression:
        if char.isdigit():
            if total == 0:
                total = int(char)
            elif symbol == "+":
                total += int(char)
            elif symbol == "*":
                total *= int(char)
        else:
            symbol = char

    return total

myfile = open("Homework.txt")
lines = myfile.readlines()
myfile.close()

answers = []

for line in lines:
    line = line.strip()
    while "(" in line:
        for i in range(len(line)):
            if line[i] == "(":
                openbrackets = i

            elif line[i] == ")":
                expression = line[openbrackets + 1:i].split(" ")

                total = completemaths(expression)

                line = list(line)
                line[openbrackets:i + 1] = str(total)    
                line = "".join(line)
                break

    expression = line.split(" ")
    total = completemaths(expression)
    answers.append(total)

final = 0
for total in answers:
    final += total

print(final)