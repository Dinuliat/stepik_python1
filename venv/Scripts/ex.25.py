n = int(input())

x = 0
y = 0
turtle = [x, y]

for i in range(n):
    w = input().split()

    if 'север' in w:
        y = y + int(w[1])

    if 'восток' in w:
        x = x + int(w[1])
    if 'юг' in w:
        y = y - int(w[1])
    if 'запад' in w:
        x = x - int(w[1])

turtle[0] = x
turtle[1] = y

print(*turtle, sep=' ')