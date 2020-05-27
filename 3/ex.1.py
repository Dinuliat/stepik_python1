# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
# например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(l):
    for i in range(len(l))[::-1]:
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            l[i] = l[i] // 2


d = [1, 4, 7, 6, 7, 5, 9, 22, 3, 56, 5, 7, 78]
modify_list(d)
print(d)