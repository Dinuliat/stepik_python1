a = int(input())
b = int(input())

y = [x for x in range(a, b + 1) if x % 3 == 0]
print(sum(y) / len(y))
