

def add(a, b):
  return a+b
def sub(a, b):
  return a-b
def multi(a, b):
  return a*b
def divide(a, b):
  return a/b
def power(a, b):
  basic = a
  for i in range(b-1):
    a = a * basic
  
  if b == 0 :
    a = 1

  return a

print("Podaj dzialanie kompatybilne z kalkulatorem google")

choose = input()

mark = choose[1]

a = int(choose[0])
b = int(choose[2])

if mark == '+':
  result = add(a, b)
  print(result)
if mark == '-':
  result = sub(a, b)
  print(result)
if mark == '*':
  result = multi(a, b)
  print(result)
if mark == '/':
  result = divide(a, b)
  print(result)
if mark == '^':
  result = power(a, b)
  print(result)


