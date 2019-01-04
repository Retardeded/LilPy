print("Podaj szerokosc choinki")
n = int(input())

width = 1
nCopy = n
height = 0

while(nCopy > 1):
  height +=  nCopy
  nCopy -= 1

sameSet = True
maxWidth = width
for i in range(height):
  if(sameSet):
    maxWidth += 1
    sameSet = False
  else:
    width += 1

  for j in range(width):
    print('x', end='')
    if(width == maxWidth ):
      width = 1
      sameSet = True
  print("")