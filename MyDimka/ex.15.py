# Пользователь вводит целое число, каждое с новой строки, до тех пор, пока не введет 666.
# После ввода каждого числа программа выводит на консоль это число, умноженное на 3.

r = 0
while r != 666:
    r = int(input())
    print(r*3)
