myfile = open("Passports.txt")
lines = myfile.readlines()
myfile.close()

passports = list()

pointer = 0
for i in range(len(lines)):
    if lines[i].strip() == "" or i == len(lines) - 1:
        passport = ""
        for j in range(pointer, i + 1):
            passport = passport + lines[j].strip() + " "

        passports.append(passport)
        pointer = i

amount = 0
for passport in passports:
   if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
       amount += 1

print(amount)
