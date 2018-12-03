import math
from random import randint

def heap_create(tab):
  numberOfNum = len(tab)
  heap_tab = []
  currentIndex = 0;
  for i in range(0, numberOfNum):
    heap_tab.append(tab[i])
    currentIndex = i
    while(currentIndex > 0):
      parentIndex = int(currentIndex/2)
      if(heap_tab[currentIndex] > heap_tab[parentIndex]):
        temp = heap_tab[currentIndex]
        heap_tab[currentIndex] = heap_tab[parentIndex]
        heap_tab[parentIndex] = temp
        currentIndex = parentIndex
      else:
        break;
  return heap_tab
def heap_sort(heap_tab):
  numberOfNum = len(heap_tab)
  sorted_tab = []
  for i in range(0, numberOfNum):
    sorted_tab.insert(0, heap_tab[0])
    heap_tab[0] = heap_tab[numberOfNum-i-1]
    currentIndex = 0
    if(heap_tab[1] > heap_tab[2]):
      parentIndex = 1
    else:
      parentIndex = 2
    while(parentIndex < numberOfNum-i and heap_tab[currentIndex] < heap_tab[parentIndex]):
      temp = heap_tab[currentIndex]
      heap_tab[currentIndex] = heap_tab[parentIndex]
      heap_tab[parentIndex] = temp
      currentIndex = parentIndex
      if(currentIndex*2+1 < numberOfNum-i and heap_tab[currentIndex*2] > heap_tab[currentIndex*2+1]):
        parentIndex = currentIndex*2
      else:
        parentIndex = currentIndex*2+1
  return sorted_tab

numberOfNum = 100
tab = []
for k in range(0, 100):
    tab.append(randint(0, 100));


print(tab)
heap_tab = heap_create(tab)
print(heap_tab)
sort_tab = heap_sort(heap_tab)
print(sort_tab)