import random

tableOfCoords = []
n = 7
m = 11

x1 = random.randint(0, n - 1)
y1 = random.randint(0, n - 1)
for k in range (10):

    for i in range (m):
        for j in range (n):
            if(max( abs(x1-j), abs(y1-i) ) == k):
                print("X", end="")
            else:
                print("0", end="")
        print("")

    print("")


