import time

def rec(num, total):
    amount = 0
    if num != lines[len(lines) - 1]:
        if num not in cache:
            for adapter in rules[num]:
                a, total = rec(adapter, total)
                amount += a
            
            cache[num] = amount
        else:
            total = total + cache[num]
            amount = cache[num]
    else:
        total += 1
        amount = 1
        
    return amount, total

start = time.time()
myfile = open("Adapters.txt")
lines = myfile.readlines()
myfile.close()

for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

lines.sort()
lines.insert(0, 0)
lines.append(lines[len(lines) - 1] + 3)
print(lines[len(lines) - 1])

rules = {}

for line in lines:
    tmp = []
    for line2 in lines:
        if line2 - 1 == line or line2 - 2 == line or line2 - 3 == line:
            tmp.append(line2)

    rules[line] = tmp

total = 0
cache = {}
amount, total = rec(0, total)

end = time.time()
print(cache)
print(total)

print("Time taken: " + str(round(end - start)) + "s")