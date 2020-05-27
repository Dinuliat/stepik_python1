a = int(input('рекомендовано для сна '))
b = int(input('не рекомендовано спать более '))
h = int(input('фактический сон '))
if a <= h < b:
    print("Это нормально")
elif h < a:
    print("Недосып")
else:
    print("Пересып")