def rod_cutting(value, length):
        if (length <= 0):
          return 0
          max = -1
          for i in range(0, length+1):
            max = max(max, value[i] + rod_cutting(value, length-i-1))
          return max
def profitDP(value, length):
		solution = [0]*(length+1)

		for i in range(1, length+1):
			maximum = -1
			for j in range(0, i):
				maximum = max(maximum, value[j] + solution[i-j-1])
				solution[i] = maximum
		return solution[length]

value = [0, 5, 8, 8, 9, 14, 16, 18, 24, 25]
print("Podaj dlugosc preta")
len = int(input())
profit = profitDP(value, len)
print("Maksymalny profit to: " + str(profit))
