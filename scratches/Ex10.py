import time
import math
start_time = time.time()
#tutaj wstaw obliczenia
numberOfNum = 2000
tab = []

for k in range(1, 21):
    start_time = time.time()
    tab = []
    tab.append(2)
    for i in range(3, numberOfNum * k):
        isPrime = True
        for j in range(len(tab) ):
            if(math.sqrt(i) < tab[j]):
                break
            if(i % tab[j] == 0):
                isPrime = False
        if(isPrime):
            tab.append(i)
    print("For numbers less than " + str(numberOfNum * k) + " Total time is")
    print("--- %s seconds ---" % (time.time() - start_time))

for i in range(0, len(tab)):
    print(": ", tab[i])