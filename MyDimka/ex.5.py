# Пользователь вводит целые числа в строку через пробел. Вывести через пробел все числа, которые больше 5.

a = [int(x) for x in input().split()]
index = 0
w = []
while index < len(a):
    if a[index] % 3 == 2:
        w.append(a[index])

    index += 1

print(*w)
