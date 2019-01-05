
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

def to_base_10(number, base):

    number_base_ten = 0
    for i in range(0, len(number)):
            number_base_ten *= base
            number_base_ten += int(number[i])

    return number_base_ten


print("Enter a base of your number")
base_def = int(input())
print("Enter a number in your base")
number_def = str(input())
transformed_number = to_base_10(number_def, base_def)
print("Enter a new base for that number")
base = int(input())
transformed_number = to_x_digits(transformed_number, base)

print("number: "+ str(number_def) + "(" + str(base_def) + ")" + " equals:")
for digit in transformed_number:
    print(digit, end='')
print("(" + str(base) + ")")


