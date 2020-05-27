# Пользователь вводит два списка целых чисел в две строки через пробел.
# Вывести через пробел отсортированный список чисел, который есть в обоих списках.

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
index_a = 0
index_b = 0
w = []
while index_a < len(a) or index_b < len(b):
    if a[index_a] == b[index_b]:
        w.append(a[index_a])
    index_a += 1
    index_b += 1

print(*w)
