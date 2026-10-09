import math

def calculate_rectangle_area(width, height):
    
    # Функция получает данные ширины и высоты, и возвращает их произведение (рассчитывает площадь прямоугольника)
    
    return width * height

def calculate_circle_area(radius):

    # Функция получает радиус окружности и возвращает её площадь

    return math.pi*radius**2

width, height = map(float, input('Введите ширину и высоту прямоугольника (через пробел) для рассчета его площади: ').split(' ')) 

print(f'Площадь прямоугольника составляет: {calculate_rectangle_area(width, height):.2f}') # Выводит площадь прямоугольника до двух знаков после запятой

radius = float(input("Введите радиус круга для расчета его площади: "))

print(f'Площадь круга составляет: {calculate_circle_area(radius):.2f}') # Выводит площадь круга до двух знаков после запятой