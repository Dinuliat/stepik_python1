g = input()
n = len(g) // 2
y = g[:n]
x = g[n:]
i = x + y
z = i[::-1]
print(z)
