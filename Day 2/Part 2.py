myfile = open("Passwords.txt")
lines = myfile.readlines()
myfile.close()

amount = 0
for line in lines:
    count = 0
    parts = line.strip().split(" ")

    parts[1] = parts[1].strip(":")

    num1, num2 = parts[0].split("-")

    if parts[2][int(num1) - 1] == parts[1] and parts[2][int(num2) - 1] != parts[1]:
        amount += 1

    elif parts[2][int(num2) - 1] == parts[1] and parts[2][int(num1) - 1] != parts[1]:
        amount += 1

print(amount)