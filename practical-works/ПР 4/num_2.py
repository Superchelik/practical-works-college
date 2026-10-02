import math

x1 = float(input("Введите x1 "))
x2 = float(input("Введите x2 "))
y1 = float(input("Введите y1 "))
y2 = float(input("Введите y2 "))

p = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

print(p)