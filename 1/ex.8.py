
x = n % 10
y = n % 100
if (10 <= n <= 20) or (110 <= n <= 120) or (210 <= n <= 220) or (310 <= n <= 320) or (410 <= n <= 420) or \
   (510 <= n <= 520) or (610 <= n <= 620) or (710 <= n <= 720) or (810 <= n <= 820) or (910 <= n <= 920):
    print(str(n) + " " + "программистов")
elif (2 <= x <= 4) or (2 <= y <= 4):
    print(str(n) + " " + "программиста")
elif (x == 1) or (y == 1):
    print(str(n) + " " + "программист")
else:
    print(str(n) + " " + "программистов")