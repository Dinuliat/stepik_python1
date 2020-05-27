# Распечатать все числа от 0 до 200 которые делятся одновременно на 2, 3 и 5

z = [int(x) for x in range(201) if x % 2 == 0 and x % 3 == 0 and x % 5 == 0]
print(*z)

# w = []
# for x in range(200+1):
#   if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
#       w.append(x)
# print(*w)
