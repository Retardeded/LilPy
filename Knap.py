
value_tab = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26]
n = 20
tab = [0] * n
for i in range(n):
    tab[i] = [0] * n

for i in range(1, n+1):
  for j in range(1, n+1):
    if(j > len(tab))