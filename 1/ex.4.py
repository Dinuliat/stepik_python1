n_1 = float(input())
n_2 = float(input())
result = str(input())
if result == "+":
    print(n_1 + n_2)
elif result == "-":
    print(n_1 - n_2)
elif result == "*":
    print(n_1 * n_2)
elif result == "pow":
    print(n_1 ** n_2)
if (n_2 == 0.0) and ((result == "/") or (result == "div") or (result == "mod")):
    print("Деление на 0! ")
if (n_2 != 0.0) and (result == "/"):
    print(n_1 / n_2)
if (n_2 != 0.0) and (result == "div"):
    print(n_1 // n_2)
if (n_2 != 0.0) and (result == "mod"):
    print(n_1 % n_2)
