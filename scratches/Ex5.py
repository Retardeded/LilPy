print("Podaj szerokosc choinki")
n = int(input())

width = 1
nCopy = n+1
height = 0

while(nCopy > 1):
  height +=  nCopy
  nCopy -= 1

sameSet = True
maxWidth = width
n = 2 * n + 1
n2 = int(n/2)
print(n2)
print(height)

for i in range(height):
  if(sameSet):
    maxWidth += 2
    sameSet = False
  else:
    width += 2
  for j in range(n):
    if(n2 <= int(j+ int(width/2) ) and j < n2):
      print('x', end='')
    elif( int(n2 + int(width/2) ) >= j and j > n2):
      print('x', end='')
    elif(j == n2):
      print('x', end='')
    else:
      print(' ', end='')
  if(width == maxWidth ):
    width = 1
    sameSet = True
  print("\n")