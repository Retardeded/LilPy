
def to_x_digits (number, base):
    transformed_number = []
    ord_A = 65
    while(number > 0):

        if(number % base < 10):
            transformed_number.insert(0, number % base)
        else:
            transformed_number.insert(0, chr(ord_A - 10 + number % base) )
        number = int(number/base)

    return transformed_number

print("Enter a number in base 10")
number = int(input())
print("Enter a new base for that number")
base = int(input())
transformed_number = to_x_digits(number, base)

print("number: "+ str(number) + " in base " + str(base) + " is ")
for digit in transformed_number:
    print(digit, end='')


