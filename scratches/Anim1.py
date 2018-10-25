import random

tableOfCoords = []
n = 7
m = 11

for k in range (10):
    x1 = random.randint(0, n-1)


    tableOfCoords.insert(0, x1)
    currentSize = len(tableOfCoords)

    for i in range (m):
        for j in range (n):
            if(i < currentSize):
                if(j == tableOfCoords[i]):
                    print("X", end="")
                else:
                    print("0", end="")
            else:
                print("0", end="")
        print("")

    print("")


