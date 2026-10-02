num_of_schoolchild = int(input("Количество школьников "))
numb_of_tangerine = int(input('Количество мандаринов '))

print("Количество мандаринов на одного школьника",numb_of_tangerine // num_of_schoolchild) #Находим сколько получит каждый (все получат поровну)
print("Количество мандаринов в корзинке",numb_of_tangerine % num_of_schoolchild) #Находим остаток от деления мандаринов на учеников