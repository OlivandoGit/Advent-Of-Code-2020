myfile = open("Seats.txt")
lines = myfile.readlines()
myfile.close()

##lines = ["FBFBBFFRLR", "FFFBBBFRRR", "BBFFBBFRLL"]

seats = []

for line in lines:
    lower = 0
    upper = 127

    for i in range(7):
        diff = round((upper - lower) / 2)
        if line[i] == "F":
            upper -= diff
            row = lower
        else:
            lower += diff
            row = upper

    lower = 0
    upper = 7

    for i in range(3):
        diff = round((upper - lower) / 2)
       
        if line[i + 7] == "L":
            upper -= diff
            col = lower
        else:
            lower += diff
            col = upper

    seatid = row * 8 + col
    seats.append(seatid)

seats.sort()

print(seats[len(seats) - 1])
