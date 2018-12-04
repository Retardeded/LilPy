from random import randint
from collections import namedtuple
import time

Digits = namedtuple("Digits", "d u")

def seletcion_sort(tab):
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

def insertion_sort(tab, b, e):
  for i in range(b+1, e):
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

def quick_sort(tab, b, e):

    pivot = tab[int((b+e)/2)]
    leftIndex = b
    rightIndex = e

    while(leftIndex <= rightIndex):
        while(pivot < tab[leftIndex]):
            leftIndex = leftIndex + 1
        while(pivot > tab[rightIndex]):
            rightIndex = rightIndex - 1

        if( leftIndex <= rightIndex):
            temp = tab[leftIndex]
            tab[leftIndex] = tab[rightIndex]
            tab[rightIndex] = temp
            leftIndex = leftIndex + 1
            rightIndex = rightIndex -1

    if (rightIndex > b):
        quick_sort(tab, b, rightIndex)
    if (leftIndex < e):
        quick_sort(tab, leftIndex, e)

def merge(tab, b, pivot, e):
    first = b
    second = pivot+1
    firstList = []
    secondList = []
    index = 0

    for i in range(b, pivot):
        firstList.append(tab[i])
    for i in range(pivot+1, e):
        secondList.append(tab[i])

    while(first < pivot+1 and second < e):
        if(firstList[first] < secondList[second]):
            tab[index] = firstList[first]
            index += 1
            first += 1
        else:
            tab[index] = secondList[second]
            index += 1
            second += 1
    while(first < pivot+1):
        tab[index] = firstList[first]
        index += 1
        first += 1
    while (second < e):
        tab[index] = secondList[second]
        index += 1
        second += 1

def merge_sort(tab, b, e):
    pivot = 0
    if(b - e > 5):
        pivot = int(b+e/2)
        merge_sort(tab, b, pivot) #
        merge_sort(tab, pivot+1, e)
        merge(tab, b, pivot, e)
    else:
        insertion_sort(tab, b, e)

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
    sorted_tab.append(heap_tab[0])
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

def bucket_sort(tab):
    n = len(tab)
    bucket_ratio = 100 / n
    array_of_buckets = []
    for i in range(0, n):
        array_of_buckets.append([])

    sorted_tab = []
    for i in range(0, n):
        index = int(tab[i]/bucket_ratio)
        array_of_buckets[index].append(tab[i])
    for i in range(0, n):
        if(len(array_of_buckets[i]) > 1):
            insertion_sort(array_of_buckets[i], 0, len(array_of_buckets[i]))
    for i in range(n-1, -1, -1):
        for j in range(0, len(array_of_buckets[i])):
            sorted_tab.append(array_of_buckets[i][j])
    return sorted_tab

def radix_sort(tab):
    n = len(tab)
    array_of_digits = [Digits] * n
    sorted_tab = []
    for i in range(0, n):
        array_of_digits[i] = Digits(int(tab[i]/10), tab[i]%10)

    array_of_digits = count_sort1(array_of_digits)

    array_of_digits = count_sort2(array_of_digits)

    for i in range(0, n):
        sorted_tab.append(int(str(array_of_digits[i].d) + str(array_of_digits[i].u)))
    return sorted_tab

def count_sort1(tab):
    n = len(tab)
    counted_digits = [0]*10
    list_of_index = [0]*10
    currentIndex = 0
    sorted_tab = [0]*n
    for i in range(0,  n):
        counted_digits[tab[i].u] += 1
    for i in range(9, -1, -1):
        list_of_index[i] = currentIndex
        currentIndex += counted_digits[i]

    for i in range(0, n):
        sorted_tab[list_of_index[tab[i].u]] = tab[i]
        list_of_index[tab[i].u] += 1
    return sorted_tab

def count_sort2(tab):
    n = len(tab)
    counted_digits = [0]*10
    list_of_index = [0]*10
    currentIndex = 0
    sorted_tab = [0]*n
    for i in range(0,  n):
        counted_digits[tab[i].d] += 1
    for i in range(9, -1, -1):
        list_of_index[i] = currentIndex
        currentIndex += counted_digits[i]

    for i in range(0, n):
        sorted_tab[list_of_index[tab[i].d]] = tab[i]
        list_of_index[tab[i].d] += 1
    return sorted_tab

numberOfNum = 500000
tab = []

for k in range(0, numberOfNum):
    tab.append(randint(0, 99))

tab_copy = tab
"""/
start_time = time.time()
bubble_sort(tab_copy)
print("Bubble sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
seletcion_sort(tab_copy)
print("Selection sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
insertion_sort(tab_copy, 0, len(tab_copy))
print("Insertion sort took: " + str(time.time()-start_time)+ " seconds")
"""
tab_copy = tab
start_time = time.time()
quick_sort(tab_copy, 0, len(tab_copy)-1)
print("Quick sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
merge_sort(tab_copy, 0, len(tab_copy)-1)
print("Merge sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
heap_tab = heap_create(tab_copy)
tab_copy = heap_sort(heap_tab)
print("Heap sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
tab_copy = bucket_sort(tab_copy)
print("Bucket sort took: " + str(time.time()-start_time)+ " seconds")
tab_copy = tab
start_time = time.time()
tab_copy = radix_sort(tab_copy)
print("Radix sort took: " + str(time.time()-start_time)+ " seconds")
