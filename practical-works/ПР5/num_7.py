print("Привествую в программе для рассчета кол-ва необходимого топлива (л.) и стоимости такси (руб.)")

distance = float(input('Введите расстояние в километрах: '))
fuel_consumption = float(input('Введите расход топлива автомобиля на 100км в литрах: '))
cost_liter_fuel = float(input('Введите текущую стоимость бензина (руб.): '))

total_num_liters = distance * (fuel_consumption / 100) # Расчет кол-ва литров за преодолённое расстояние
total_cost = total_num_liters * cost_liter_fuel # Итоговая стоимость такси за поездку

print(f'Потребуется {total_num_liters:.2f} л. бензина') 
print(f'Поездка составит {total_cost:.2f} руб.') 