numbers = [0,5,4,1,10,14,7]

spoken = {}

for i in range(len(numbers)):
    spoken[numbers[i]] = i

for i in range(len(numbers) - 1, 30000000):
    if numbers[i] not in spoken.keys():
        numbers.append(0)
    else:
        numbers.append(i - spoken[numbers[i]])
    
    spoken[numbers[i]] = i

print(numbers[30000000-1])