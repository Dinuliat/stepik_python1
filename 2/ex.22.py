g = input()
g = g[::-1]
cnt = 0
len_of_g = len(g)
n = len(g)//2
x = g[:n]
y = g[n:-1]
print(y+x)


