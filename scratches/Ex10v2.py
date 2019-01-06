import time
import math

def strainer(table, n):
    for i in range(2, len(table)):
        if(table[i] == 0):
            for j in range(i*i, n, i):
                table[j] = 1




start_time = time.time()
#tutaj wstaw obliczenia
numberOfNum = 3000
tab = []

for k in range (1, 21):
    start_time = time.time()
    n = numberOfNum * k * k
    tab = [0] * n
    strainer(tab, n)

    for i in range (2, len(tab)):
        if(tab[i] == 0):
            tab[i] = tab[i]
    print("For numbers less than " + str(n) + " Total time is")
    print("--- %s seconds ---" % (time.time() - start_time))

    if(k == 20):
        for i in range(2, len(tab)):
            if (tab[i] == 0):
                print(": ", i)
