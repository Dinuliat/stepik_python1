# Пользователь вводит целые числа в строку через пробел. Вывести сумму нечетных чисел.

a = [int(x) for x in input().split()]
s = 0
index = 0
while index < len(a):
    if a[index] % 2 != 0:
        s += a[index]
    index += 1
print(s)