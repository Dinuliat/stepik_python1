# Польхователь вводит целые числа в одну строку разделенные пробелом. Программа должна распечатать числа:
# каждое число в отдельной строке.

cat = input().split()
print(*cat, sep = "\n")
