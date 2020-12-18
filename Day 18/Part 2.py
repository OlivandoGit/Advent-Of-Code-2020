def completemaths(expression):
    while "+" in expression:
        for i in range(len(expression)):
            if expression[i] == "+":
                total = int(expression[i - 1]) + int(expression[i + 1])
                
                for j in range(3):
                    del expression[i - 1]

                expression.insert(i - 1, str(total))
                break            

    total = 1
    for char in expression:
        if char.isdigit():
            total *= int(char)

    return total

myfile = open("Homework.txt")
lines = myfile.readlines()
myfile.close()

answers = []

for line in lines:
    print(line)
    print()
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
                print(line)
                print()
                break

    expression = line.split(" ")
    total = completemaths(expression)
    answers.append(total)

final = 0
for total in answers:
    final += total

print(final)