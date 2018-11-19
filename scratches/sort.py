import math
from random import randint

def choose_sort(tab):
  numberOfNum = len(tab)
  for i in range(0, numberOfNum):
    max = tab[i]
    indexMax = i
    for j in range(i, numberOfNum):
      if(max < tab[j]):
        max = tab[j]
        indexMax = j
    temp = tab[i]
    tab[i] = max
    tab[indexMax] = temp

def set_sort(tab):
  numberOfNum = len(tab)
  for i in range(1, numberOfNum):
    value = tab[i]
    index = i
    while(index > 0 and tab[index-1] < value):
      tab[index] = tab[index-1]
      index = index-1

    if(index < i):
      tab[index] = value

def set_sort(tab):
  numberOfNum = len(tab)
  for i in range(1, numberOfNum):
    value = tab[i]
    index = i
    while(index > 0 and tab[index-1] < value):
      tab[index] = tab[index-1]
      index = index-1

    if(index < i):
      tab[index] = value

def bubble_sort(tab):
  numberOfNum = len(tab)
  for i in range(0, numberOfNum-1):
    swap = False
    for j in range(1, numberOfNum-i):
      if(tab[j] > tab[j-1]):
        temp = tab[j-1]
        tab[j-1] = tab[j]
        tab[j] = temp
        swap = True
    if(swap == False):
      break

numberOfNum = 100
tab = []

for k in range(0, 100):
    tab.append(randint(0, 100));


print(tab)
bubble_sort(tab)

print(tab)