a = [int(x) for x in input().split()]
#   b = sorted(a)
s = []
for x in a:
    if a.count(x) > 1 and x not in s:
        s.append(x)
print(*s)
