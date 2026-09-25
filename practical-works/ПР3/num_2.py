my_list=[1,2,3]
print(my_list)
my_list[0] = 99
print(my_list)
#Список изменился, так как списки являются изменяемыми объектами.

my_tuple=(1,2,3)
print(my_tuple)
my_tuple[0] = 99  # TypeError: 'tuple' object does not support item assignment
#Кортеж не изменился, так как кортежи являются неизменяемыми объектами.

my_string="cat"
print(my_string)
my_string[0] = "b"  # TypeError: 'str' object does not support item assignment
#Строка не изменилась, так как строки являются неизменяемыми объектами.