import re

def getregex(rule):
    rule = rules[rule]
    if "|" in rule:
        part1 = [int(i) for i in (rule[:rule.index("|") - 1]).split(" ")]
        part2 = [int(i) for i in (rule[rule.index("|") + 2:]).split(" ")]

        regex1 = "(" + ")(".join([getregex(i) for i in part1]) + ")"
        regex2 = "(" + ")(".join([getregex(i) for i in part2]) + ")"

        result =  "(" + regex1 + ")|(" + regex2 + ")"
        
    elif '"' in rule:
        result = rule[1]

    else:
        parts = [int(i) for i in rule.split(" ")]
        result = "(" + ")(".join([getregex(i) for i in parts]) + ")"

    return result

myfile = open("Passwords.txt")
lines = myfile.readlines()
myfile.close()

rules = {}

for line in lines[:lines.index("\n")]:
    name, rule = line.strip().split(": ")

    rules[int(name)] = rule

lines = lines[lines.index("\n") + 1:]

regex = getregex(0)

matches = 0
for password in lines:
    if bool(re.fullmatch(regex, password.strip())):
        matches += 1

print(matches)