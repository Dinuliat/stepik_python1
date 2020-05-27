f = int(input())
s = f
while f != 0:
    f = int(input())
    s += f
    if f == 0:
        print(s)