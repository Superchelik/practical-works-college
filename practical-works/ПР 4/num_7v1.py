comp_carriage = {
    "Купе 1": [1,2,3,4],
    "Купе 2": [5,6,7,8],
    "Купе 3": [9,10,11,12],
    "Купе 4": [13,14,15,16],
    "Купе 5": [17,18,19,20],
    "Купе 6": [21,22,23,24],
    "Купе 7": [25,26,27,28],
    "Купе 8": [29,30,31,32],
    "Купе 9": [33,34,35,36]
}

seat_number=int(input('Введите номер места: '))

for compartement, seats_list in comp_carriage.items():
    if seat_number in seats_list:
        print(compartement)
        break
else:
    print("Такого места нет")