x = int(input())
h = int(input())
m = int(input())
minute = int((m + (x % 60)) % 60)
hour = int(h + (x//60) + (m + (x % 60)) // 60)
print(hour)
print(minute)

