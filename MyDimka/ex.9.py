# Программа должна решать линейное уравнение a * x + b = 0.
# Пользователь вводит через пробел дробные числа a и b.
# Программа должна вывести найденное значение x или, если его нет, написать "Решений нет".
# Если решений бесконечное множество, программа должна написать "x - любое число".

a, b = [float(x) for x in input("Введите два дробных числа: ").split()]
if a == 0 and b == 0:
    print("x - любое число")
elif a == 0 and b != 0:
    print("решения нет")
elif a != 0:
    x = (-b) / a
    print(x)







