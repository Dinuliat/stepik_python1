# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.

# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
# Если и ключа 2 * key нет, нужно добавить ключ 2 * key в словарь и сопоставить ему список из переданного элемента [value].

# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    if key not in d:
        if key*2 not in d:
            d.update({key*2: [value]})
        else:
            d[key*2].append(value)

f = {}
update_dictionary(f, 2, 3)
update_dictionary(f, 2, 5)
print(f)

