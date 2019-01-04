import time

def pascal_recursive(height):
    row = []
    if(height == 1):
        row = [1]
    else:
        last_row = pascal_recursive(height-1)
        n = height
        for i in range(n):
            if( i == 0 or i == n-1):
                row.append(1)
            else:
                row.append(last_row[i-1] + last_row[i])
    print(row)
    return row

print("Podaj wysokosc trojkata Pascala")
number = int(input())
start = time.time()
pascal_recursive(number)
print("Czas wynosi: " + str(time.time() - start))