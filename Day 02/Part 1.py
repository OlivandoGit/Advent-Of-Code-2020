myfile = open("Passwords.txt")
lines = myfile.readlines()
myfile.close()

amount = 0
for line in lines:
    count = 0
    parts = line.strip().split(" ")

    parts[1] = parts[1].strip(":")

    num1, num2 = parts[0].split("-")

    for char in parts[2]:
        if char == parts[1]:
            count += 1

    if count >= int(num1) and count <= int(num2):
        amount += 1

print(amount)