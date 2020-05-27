# Пользователь вводит два списка целых чисел в две строки через пробел.
# Вывести через пробел отсортированный список чисел, который есть в обоих списках.

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = a + b
c.sort()

print(*c)

#ind = 0
#w = []
#for i in range(len(c)):
#    if i[ind] == i[::ind+1]:
#        w.append(i[ind])
#    ind += 1
#print(*w)





