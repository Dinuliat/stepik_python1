# Пользователь вводит целое число.
# Необходимо вывести треугольник из звездочек, в основании которого лежит то, количество звездочек, которое ввел пользователь.
# Например, пользователь ввел 5. Программа должна вывести:

# *
# **
# ***
# ****
# *****

w = int(input())
c = 1
while c <= w:
    print("*" * c)
    c += 1

#for c in range(1, w+1):
    #print("*" * c)
    #c += 1




