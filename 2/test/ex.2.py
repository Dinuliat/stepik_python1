# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (
# число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить
# программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

n = int(input())
e = []
for i in range(n):
    j = 0
    while j < i + 1:
        e.append(i + 1)
        j += 1
    if len(e) > n:
        break
e = e[0:n]
for i in e:
    print(i, end=" ")
