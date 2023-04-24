data = open('2022/inputFiles/data1.txt', 'r')
#elfNmbr = 0
def partOne(data):
    mostCalories = 0
    tempCalories = 0

    while True:
        line = data.readline()
        if not line:
            break
        elif len(line.strip()) == 0:
            if(tempCalories > mostCalories):
                mostCalories = tempCalories
            tempCalories = 0
        else:
            tempCalories += int(line)

    data.close()

    print("the elf with the most number of calories has ", mostCalories, " calories")

def partTwo(data):
    topCal = [0,0,0]
    tempCal = 0
    while True:
        line = data.readline()
        if not line:
            break
        elif len(line.strip()) == 0:
            if(tempCal > min(topCal)):
                topCal[topCal.index(min(topCal))] = tempCal
            tempCal = 0
        else:
            tempCal += int(line)

    print("the sum of the calories of the three elves with the most amount of calories is ", sum(topCal))

partTwo(data)
