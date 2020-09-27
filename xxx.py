n = int(input())

new_list = []

search_no = True

for i in range(n):
    nn = input()
    new_list.append(nn)

k = int(input())

for x in range(k):
    word = input()

    fin_list = []
    for line in new_list:
        if word.lower() in line.lower():
            search_no = False
            fin_list.append(line)

print(*fin_list, sep='\n')