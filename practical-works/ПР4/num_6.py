import math

x = float(input("Введите значение (градусы) "))

x = math.radians(x)

result_of_expr = math.sin(x) + math.cos(x) + (math.tan(x)**2)

print(result_of_expr)