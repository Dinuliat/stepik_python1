# Пользователь вводит дробные числа через пробел в одну строку.
# Неободимо вывести через пробел все числа, больше 10

a = [float(x) for x in input("Введите дробные числа: ").split()]
#r = []
#for x in a:
   # if x > 10:
    #   r.append(x)
#print(*r)

w = [x for x in a if x > 10]
e = len(w)

print(e)