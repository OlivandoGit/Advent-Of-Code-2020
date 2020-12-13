myfile = open("Busses.txt")
lines = myfile.readlines()
myfile.close()

mytime = int(lines[0].strip())

soonest = 0
wait = mytime

for time in lines[1].split(","):
    if time != "x":
        time = int(time)
        tmp = 0
        
        while tmp < mytime:
            tmp += time

        tmp -= mytime

        if tmp < wait:
            wait = tmp
            soonest = time

print(soonest * wait)