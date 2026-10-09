withdrawal_amount = int(input('Введите сумму, которую хотите снять (Доступны купюры: 5000 2000 1000 500 200 100): ')) #Ввод суммы

thousands = withdrawal_amount // 1000 # Количество 1000

five_thousands = thousands // 5 # рассчет сколько 5000 в сумме
two_thousands = (thousands - five_thousands * 5) // 2 # рассчет сколько 2000 в сумме (если из суммы вычесть количество 5000)
one_thousands = (thousands - five_thousands * 5 - two_thousands * 2) // 1 # рассчет сколько 1000 в сумме (если из суммы вычесть количество 5000 и 2000)

hundreds = (withdrawal_amount - thousands * 1000) // 100 # Количество 100 (если из начальной суммы вычесть все тысячи)

five_hundreds = hundreds // 5 # рассчет сколько 500 в сумме (если из начальной суммы вычесть все 1000)
two_hundreds = (hundreds - five_hundreds * 5) // 2 # рассчет сколько 200 в сумме (если из начальной суммы вычесть все 1000 и 500)
one_hundreds = (hundreds - five_hundreds * 5 - two_hundreds * 2) # рассчет сколько 100 в сумме (если из начальной суммы вычесть все 1000, 500 и 200)

print('Банкоматом будет выдано:')
print(f"Количество купюр номиналом 5000: {five_thousands}")
print(f"Количество купюр номиналом 2000: {two_thousands}")
print(f"Количество купюр номиналом 1000: {one_thousands}")
print(f"Количество купюр номиналом 500: {five_hundreds}")
print(f"Количество купюр номиналом 200: {two_hundreds}")
print(f"Количество купюр номиналом 100: {one_hundreds}")