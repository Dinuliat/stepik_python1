a = int(input())
b = int(input())
s = 0
n = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        n += 1
        s += i
t = s / n
print(t)

