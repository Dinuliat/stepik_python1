# Пользователь вводит целое число n.
# Необходимо найти сумму ряда: 1 - 1/4 + 1/9 - 1/16 + 1/25 - 1/36 +  ... + 1/n**2.

n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        w = -1 / (i**2)
        s += w
    else:
        w = 1 / (i**2)
        s += w
print(s)



print(1 - 1/(2*2) + 1/(3*3) - 1/(4*4) + 1/(5*5) - 1/(6*6) + 1/(7*7))