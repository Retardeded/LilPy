print("Enter number in base 2")

number = str(input())
number_base_ten = 0
for i in range(0, len(number)):
    number_base_ten *= 2
    number_base_ten += int(number[i])

print("number: "+ str(number) + "(2) in base 10 is " + str(number_base_ten))