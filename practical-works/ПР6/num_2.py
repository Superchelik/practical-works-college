GREEN_NUMBER = 0 # зелёный цвет рулетки
red_number = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36) # красные цвета рулетки
black_number = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35) # черные цвета рулетки

number = int(input('Введите число рулетки для определения цвета (0-36): '))

if number in red_number:
    print('Ваше число красное')

elif number in black_number:
    print('Ваше число черное')

elif number == GREEN_NUMBER:
    print('Ваше число зелёное')

else:
    print('Ошибка ввода')