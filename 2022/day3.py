data = open('2022/inputFiles/data3.txt', 'r')
diff_lower = ord('a') - 1
diff_capital = ord('A') -27


def partOne(data):

    sum = 0

    while True:
        line = data.readline()
        if not line:
            break
        split = int(len(line)/2)
        first_half = line[:split]
        second_half = line[split:]
        for c in first_half:
            if c in second_half:
                if(c.islower()):
                    sum += ord(c) - diff_lower
                else:
                    sum += ord(c) - diff_capital
                break
    print("the sum is ", sum)

def partTwo(data):
    sum2 = 0
    while True:
        line1 = data.readline()
        if not line1:
            break
        line2 = data.readline()
        line3 = data.readline()

        for c in line1:
            if c in line2 and c in line3:
                if(c.islower()):
                    sum2 += ord(c) - diff_lower
                else:
                    sum2 += ord(c) - diff_capital
                break
    
    print("the sum is", sum2)

partTwo(data)
data.close()