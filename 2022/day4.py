data = open('2022/inputFiles/data4.txt', 'r')

def sign(val):
    if(val < 0):
        return -1
    elif(val == 0):
        return 0
    else:
        return 1
    
def diff(val1, val2):
    return int(val1) - int(val2)
    
def partOne(data):
    # A pair is fully contained if the sign on the difference of the beginnings 
    # and the endings are different or if the pairs are exaclty the same
    
    fully_contained = 0
    
    while True:
        line = data.readline()
        if not line:
            break

        words = line.strip().split(",")
        word1 = words[0].split('-')
        word2 = words[1].split('-')

        if (sign(diff(word1[0], word2[0])) != sign(diff(word1[1], word2[1]))):
            fully_contained += 1
        elif(sign(diff(word1[0], word2[0])) == 0):
            fully_contained += 1

    data.close()
    print("the number of fully cointained pairs are: ", fully_contained)


def between(lim1, lim2, val):
    if(int(lim1) <= int(val) and int(val) <= int(lim2)):
        return True

def partTwo(data):
    # A pair is fully contained if the sign on the difference of the beginnings 
    # and the endings are different or if the pairs are exaclty the same

    overlapping = 0

    while True:
        line = data.readline()
        if not line:
            break

        words = line.strip().split(",")
        word1 = words[0].split('-')
        word2 = words[1].split('-')

        if(between(word1[0], word1[1], word2[0] or between(word1[0], word1[1], word2[1]))): 
            #checks if word2 overlaps word1
            overlapping += 1
        elif(between(word2[0], word2[1], word1[0] or between(word2[0], word2[1], word1[1]))):
            #checks if word1 overlaps word2
            overlapping += 1

    data.close()
    print("the number of overlapping pairs are: ", overlapping)

partTwo(data)

