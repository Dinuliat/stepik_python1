# Пользователь вводит через пробел три стороны треугольника.
# Определите, лежат ли эти стороны на одной прямой или нет.
# Подсказка: у треугольника сумма любых двух сторон больше третьей

a, b, c = [int(x) for x in input("Введите три стороны треугольника: ").split()]
if (a + b) > c and (b + c) > a and (a + c) > b:
    print("Стороны не лежат на одной прямой")
else:
    print("Стороны лежат на одной прямой")


