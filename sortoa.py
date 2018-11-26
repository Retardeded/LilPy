import math
from random import randint

def quick_sort(tab, p, k):
  pivot = tab[p]
  currentPosition = p
  for i in range(p+1, k):
    
     if(tab[i] > pivot):
       temp = tab[i]
       tab[i] = tab[currentPosition]
       tab[currentPosition] = temp
       currentPosition = currentPosition + 1

  temp = tab[currentPosition]
  tab[currentPosition] = pivot
  tab[p] = temp

  if(p < currentPosition - 1):
    quick_sort(tab, p, currentPosition - 1)
  if(currentPosition + 1 < k):
    quick_sort(tab, currentPosition + 1, k)

numberOfNum = 100
tab = []

for k in range(0, 100):
    tab.append(randint(0, 100));

print(tab)
quick_sort(tab, 0, len(tab))

print(tab)