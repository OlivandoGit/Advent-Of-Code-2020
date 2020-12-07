myfile = open("Bags.txt")
lines = myfile.readlines()
myfile.close()

layers = [["shiny gold"]]

layer = 0

while True:
    tmp = []
    for line in lines:
        bag, contains = line.split(" bags contain")
        for colour in layers[layer]:
            if colour in contains:
                tmp.append(bag)

    if len(tmp) > 0:
        layers.append(tmp)
        layer += 1
    else:
        break

layers2 = []
for layer in layers:
    for bag in layer:
        if bag not in layers2:
            layers2.append(bag)

print(len(layers2) - 1)