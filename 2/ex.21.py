genom = input()
cnt = 0
for c in genom:
    c = c.lower()
    if c == 'c' or c == 'g':
        cnt += 1
e = (cnt/len(genom))*100
print(e)
