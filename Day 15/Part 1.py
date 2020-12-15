numbers = [0,5,4,1,10,14,7]

for i in range(len(numbers) - 1, 2020):
    try:
        index = numbers[::-1][1:].index(numbers[i]) + 1
        index = (len(numbers) - 1) - index
        numbers.append(i - index)
    except ValueError:
        numbers.append(0)

print(numbers[2020-1])