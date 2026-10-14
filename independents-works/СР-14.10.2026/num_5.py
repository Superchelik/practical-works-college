color_1, color_2 = map(str, input('Введите через пробел два цвета из трёх основных (красный синий жёлтый): ').split(' '))

if color_1 == 'красный' and color_2 == 'жёлтый' or color_1 == 'жёлтый' and color_2 == 'красный':
    print('Получится оранжевый цвет')

elif color_1 == 'жёлтый' and color_2 == 'синий' or color_1 == 'синий' and color_2 == 'жёлтый':
    print('Получится зелёный цвет')

elif color_1 == 'красный' and color_2 == 'синий' or color_1 == 'синий' and color_2 == 'красный':
    print('Получится фиолетовый цвет')

else:
    print('Введены некорректные цвета')