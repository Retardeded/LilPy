def fib(n, tab):
  if(len(tab) > n):
    return tab[n-1]
  elif (n == 0):
    tab.append(1)
    return 1
  elif (n ==1):
    tab.append(1)
    return 1
  else:
    tab.append(fib(n-1, tab) + fib(n-2, tab))
    return tab[n-1]

tab = []
value = fib(10-1, tab)
print(value)
