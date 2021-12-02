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
    parts = passport.split(" ")
    valid = 0
    for part in parts:
        if len(part) > 0:
            name, data = part.split(":")

            if name == "byr":
                if data.isdigit():
                    if int(data) >= 1920 and int(data) <= 2002:
                        valid += 1

            if name == "iyr":
                if data.isdigit():
                    if int(data) >= 2010 and int(data) <= 2020:
                        valid += 1
            
            if name == "eyr":
                if data.isdigit():
                    if int(data) >= 2020 and int(data) <= 2030:
                        valid += 1

            if name == "hgt":
                measure = data[len(data) - 2:]
                height = data[:len(data) - 2]
                if height.isdigit():
                    if measure == "cm":
                        if int(height) >= 150 and int(height) <= 193:
                            valid += 1

                    elif measure == "in":
                        if int(height) >= 59 and int(height) <= 76:
                            valid += 1

            if name == "hcl":
                if data[0] == "#" and len(data) == 7:
                    try:
                        int(data[1:], 16)
                        valid += 1

                    except any:
                        continue
                
            if name == "ecl":
                if data == "amb" or data == "blu" or data == "brn" or data == "gry" or data == "grn" or data == "hzl" or data == "oth":
                    valid += 1

            if name == "pid":
                if len(data) == 9 and data.isdigit():
                    valid += 1

    if valid == 7:
        amount += 1

print(amount)
