
f = open('D:\SCM\stepik_python1\dataset_3380_5 (4).txt', 'r', encoding='utf-8')

lines = f.readlines()

counts = dict()
heights = dict()

for line in lines:
    vals = line.split()
    c = int(vals[0])
    h = int(vals[2])

    if c not in counts:
        counts[c] = 1
    else:
        counts[c] = counts[c] + 1

    if c not in heights:
        heights[c] = h
    else:
        heights[c] = heights[c] + h

for i in range(1, 12):
    if i in counts:
        count = counts[i]
        h = heights[i]
        avg = h/count
        print(i, avg)
    else:
        print(i, '-')

f.close()