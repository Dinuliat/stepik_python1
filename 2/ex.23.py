genom = input().lower()

count = 0
total = 0
for x in genom:
    total += 1
    if x == 'c' or x == 'g':
        count += 1
e = 100 * count / total
print(e)
