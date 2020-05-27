g = input()
r = ""
i = 0
len_of_g = len(g)
while i < len(g):
        j = 0
        current = g[i]
        while i < len(g) and g[i] == current:
            i += 1
            j += 1
        r += current + str(j)
print(r)
