# Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
# выходящей из левого верхнего угла и закрученной против часовой стрелки.

m = int(input())
matrix = [[0] * m for i in range(m)]
#print(*matrix)

x = 0
y = 0
s = 1
while s < m**2:
    while x < m -1 and matrix[x+1][y] == 0:
        matrix[x][y] = s
        x += 1
        s += 1
# print(*matrix, sep = '\n')

    while y < m-1 and matrix[x][y+1] == 0:
        matrix[x][y] = s
        y += 1
        s += 1
# print(*matrix, sep = '\n')

    while x > 0 and matrix[x-1][y] == 0:
        matrix[x][y] = s
        x -= 1
        s += 1
#print(*matrix, sep = '\n')

    while y > 0 and matrix[x][y-1] == 0:
        matrix[x][y] = s
        y -= 1
        s += 1
#print(*matrix, sep = '\n')

matrix[x][y] = s
for t in matrix:
    print(*t)