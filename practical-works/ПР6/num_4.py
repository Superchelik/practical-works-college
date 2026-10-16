first_position_1, first_position_2 = map(int, input('Укажите начальную позицию слона на шахматной доске (число число): ').split(' '))
second_position_1, second_position_2 = map(int, input('Укажите позицию, куда хотите пойти слоном на шахматной доске (число, число): ').split(' '))

if abs(first_position_1 - second_position_1) == abs(first_position_2 - second_position_2):
    print('YES')
else:
    print('NO')