# Пользователь вводит через пробел 3 числа:
# Первое число - количество рублей на счету
# Второе число - количество лет
# Третье число - годовая процентная ставка для счета
#
# Программа должна посчитать, сколько рублей будет на этом счету по истечении указанного количества лет

money = int(input("Сумма на счету (руб): "))
year = int(input("Срок вклада (лет): "))
bonus = int(input("Годовая процентная ставка: "))
b = (1 + bonus / 100)
su = money
for z in range(1, year+1):
    su = su * b

print("Cумма на счету с учетом % по истечению срока вклада: " + str(su))

