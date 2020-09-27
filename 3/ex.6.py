
n = int(input())

count_3 = 0
count_coupe = 0
count_last = 0
count_sum_5 = 0
count_05 = 0
count_7 = 1

count_last_2 = 0
last_2 = n%10

while n != 0:
    last = n % 10

    if last == 3:
        count_3 += 1

    if last % 2 == 0:
        count_coupe += 1

    if last > 5:
        count_sum_5 += last

    if last == 0 or last == 5:
        count_05 += 1

    if last > 7:
        count_7 *= last

    if last_2 == last:
        count_last_2 += 1

    n = n // 10


print(count_3)
print(count_last_2)
print(count_coupe)
print(count_sum_5)
print(count_7)
print(count_05)


