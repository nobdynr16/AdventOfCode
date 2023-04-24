def partOne():
    points = 0
    pointMap = {
        "A" : 1, 
        "X" : 1, 
        "B" : 2, 
        "Y" : 2, 
        "C" : 3, 
        "Z" : 3, 
    }

    with open('2022/inputFiles/data2.txt') as f:
        for line in f:
            row = line.strip().split()
            points += pointMap.get(row[1])
            score = pointMap.get(row[0]) - pointMap.get(row[1])
            if score == 0:
                points += 3
            elif score == -1 or score == 2:
                points += 6

    print("my total score is ", points)


def partTwo():
    points = 0
    pointMap = {
        "A" : 1, 
        "X" : 1, 
        "B" : 2, 
        "Y" : 2, 
        "C" : 3, 
        "Z" : 3, 
    }
    add = 0

    with open('2022/inputFiles/data2.txt') as f:
        for line in f:
            row = line.strip().split()

            if(row[1] == "X"):
                add = pointMap.get(row[0]) + 2
            elif(row[1] == "Y"):
                points += 3
                add = pointMap.get(row[0])
            else:
                points += 6
                add = pointMap.get(row[0]) + 1 

            #print("add: ", add)
            if add > 3:
                add -= 3
            points += add
            #print(points)

    print("my total score is ", points)

partTwo()



        