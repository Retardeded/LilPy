import time

def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    elif n == 1:
        return 1
    else:
        return 0

def fib_iterate(n):
    before_2 = 0
    before_1 = 1
    number = 0
    if n >=2:
        for i in range(2, n+1):
            number = before_1 + before_2
            before_2 = before_1
            before_1 = number
    elif n == 1:
        return 1
    else:
        return 0

    return number

print("Podaj numer wyrazu ciągu fib")
number = int(input())
start = time.time()
print(str(number) + " wyraz ciagu wynosi: " + str(fib(number)))
print("Czas rekurencji wynosi: " + str(time.time() - start))
start = time.time()
print(str(number) + " wyraz ciagu wynosi: " + str(fib_iterate(number)))
print("Czas iteracji wynosi: " + str(time.time() - start))