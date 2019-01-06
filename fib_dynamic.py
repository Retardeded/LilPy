import time

def fib(n, tab):
  if(len(tab) > n):
    return tab[n]
  else:
    tab.append(fib(n-2, tab) + fib(n-1, tab))
    return tab[n]

tab = [0, 1]
print("Podaj numer wyrazu ciągu fib")
number = int(input())
start = time.time()

value = fib(number, tab)
print(str(number) + " wyraz ciagu wynosi: " + str(value))
print("Czas dynamicznej rekurencji wynosi: " + str(time.time() - start))