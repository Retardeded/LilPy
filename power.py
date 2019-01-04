import  time

def power(n):
    if n > 1:
        return  n*power(n-1)
    else:
        return 1

def power_iterate(n):
    number = 1
    for i in range(1, n+1):
        number *= i
    return  number

print("Podaj liczbe")
number = int(input())
start = time.time()
print(str(number) + " silnia wynosi: " + str(power(number)))
print("Czas rekurencji wynosi: " + str(time.time() - start))
start = time.time()
print(str(number) + " silnia wynosi: " + str(power_iterate(number)))
print("Czas iteracji wynosi: " + str(time.time() - start))