
h = int(input())
x = int(input())
y = int(input())

in_day = x - y
way = h - x

rezult = way // in_day + way % in_day
if way % in_day == 0 :
    rezult += 1

print(rezult)
