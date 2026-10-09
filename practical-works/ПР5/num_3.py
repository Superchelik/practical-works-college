USD_TO_RUB = 85.00 # Курс доллара к рублю

def convert_usd_to_rub(amount_usd): 

    # Функция переводит доллары в рубли и возвращает значение в рублях

    return amount_usd * USD_TO_RUB

amount_usd = float(input('Введите сумму в долларах, для перевода в рубли: ')) # Вводим сумму в долларах

amount_usd = convert_usd_to_rub(amount_usd) # присваиваем этой же переменной расчитанное значение в функции

print(f'Ваша сумма в рублях составляет: {amount_usd}') # Вывод в рублях