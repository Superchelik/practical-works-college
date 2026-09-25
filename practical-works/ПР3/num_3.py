#Если ввести слова или числа с плавающей точкой, то будет ошибка
#ValueError: invalid literal for int() with base 10: 'abc'
try:
  num1 = int(input())
  num2 = int(input())
  result = num1 + num2
  print(result)

except ValueError:
  print("Нельзя использовать буквы или числа с плавающей точкой. Введите целые числа.")