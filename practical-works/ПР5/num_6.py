import math

def calc_distance(x1, y1, x2, y2):

    # Функция вычисляет сторону треугольника по координатам двух вершин и возвращает полученное значение

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance

def calc_triangle_area(a, b, c):

    # Функция вычисляет площадь треугольника по трём сторонам (формула Герона) и возвращает полученное значение

    p = (a + b + c) / 2 # полупериметр
    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) #площадь

    return area

x_a, y_a, x_b, y_b, x_c, y_c = map(float, input('Введите координаты вершин треугольника (x1 y1 x2 y2 x3 y3): ').split(' '))

a = calc_distance(x_a, y_a, x_b, y_b) # Указываны координаты вершин a и b
b = calc_distance(x_b, y_b, x_c, y_c) # Указываны координаты вершин b и c
c = calc_distance(x_c, y_c, x_a, y_a) # Указываны координаты вершин c и a

area = calc_triangle_area(a, b, c) # Указаны посчитанные стороны

print(f'Площадь треугольника = {area:.2f}. Значение округлено до сотых')