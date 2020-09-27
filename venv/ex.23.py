n = int(input())

words = []
for i in range(n):
    w = input()
    w = w.lower()
    words.append(w)

s = int(input())
lines = []

for i in range(s):
    sentence = input()
    sentence = sentence.lower()
    lines.append(sentence)

errors = []
for line in lines:
    words_in_line = line.split()
    for w2 in words_in_line:
        if w2 not in words:
            errors.append(w2)

errors = set(errors)
print(*errors, sep='\n')
