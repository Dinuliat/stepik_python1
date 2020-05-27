shape = str(input())
if shape == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    s_triangle = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(s_triangle)
if shape == "круг":
    r = int(input())
    z = 3.14
    s_circle = float(z * r**2)
    print(s_circle)
if shape == "прямоугольник":
    a = int(input())
    b = int(input())
    s_rectangle = float(a * b)
    print(s_rectangle)
