
src = input()
encoded = input()

line = input()
line2 = input()

encoder = dict()
decoder = dict()

for i in range(len(src)):
    from_char = src[i]
    to_char = encoded[i]

    encoder[from_char] = to_char
    decoder[to_char] = from_char

for x in line:
    y = encoder[x]
    print(y, end='', sep='')
print()

for x in line2:
    y = decoder[x]
    print(y, end='', sep='')
