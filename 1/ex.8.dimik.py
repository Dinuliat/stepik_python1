n = int(input())
x = n % 10
y = n % 100
if y == 11 or y == 12 or y == 13 or y == 14:
    print(str(n) + ' программистов')
elif x == 1:
    print(str(n) + ' программист')
elif x == 2 or x == 3 or x == 4:
    print(str(n) + ' программиста')
else:
    print(str(n) + ' программистов')
