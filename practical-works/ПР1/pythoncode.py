import random

# Компьютер загадывает число от 1 до 20
secret_number = random.randint(1, 20)
print("Я загадал число от 1 до 20. Попробуй угадать его!")

# Даем игроку 5 попыток
for attempts in range(1, 6):
    guess = int(input(f"Попытка №{attempts}. Введите ваше число: "))
    
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число за {attempts} попыток!")
        break
else:
    print(f"К сожалению, попытки закончились. Я загадал число {secret_number}.")
