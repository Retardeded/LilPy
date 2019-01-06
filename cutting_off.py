from random import randint
from collections import namedtuple
import time
import math

Digits = namedtuple("Digits", "p h")

def markPrime(array_of_stats, numbers):
    n = len(numbers)
    for i in range(0, n):
        if(numbers[i] != 1):
            array_of_stats[numbers[i]] = Digits(1, array_of_stats[numbers[i]].h)
        for j in range(2, n):
            if (math.sqrt(numbers[i]) < j):
                break
            if (numbers[i] % j == 0):
                array_of_stats[numbers[i]] = Digits(0, array_of_stats[numbers[i]].h)
                break

def countNumbers(array_of_stats, numbers):
    n = len(numbers)
    for i in range(n):
        value = array_of_stats[numbers[i]].h + 1
        array_of_stats[numbers[i]] = Digits(array_of_stats[numbers[i]].p, value)

numbers = [int(x) for x in input().split()]
#[5, 7, 4, 18, 3, 7, 5, 1, 2, 12, 7, 13]
m = len(numbers)
n = 0
for i in range(m):
    if(numbers[i] > n):
        n = numbers[i]

n = n + 1

array_of_stats = [Digits] * n
for i in range(0, n):
    array_of_stats[i] = Digits(0, 0)

n = len(numbers)
markPrime(array_of_stats, numbers)
countNumbers(array_of_stats, numbers)
for i in range(0, n):
    if(array_of_stats[numbers[i]].p == 0 or array_of_stats[numbers[i]].h % 2 == 0):
        print(numbers[i])
