fuel_consumption_for_100_kilometers = 6.2
fuel_left = 0.54
fuel_tank_liters = 40

fuel_left_liters = fuel_left * fuel_tank_liters
fuel_consumption_for_1_kilometer = fuel_consumption_for_100_kilometers / 100

# округлим до 2х знаков после запятой
kilometers_can_drive = round(fuel_left_liters/fuel_consumption_for_1_kilometer, 2)

print(kilometers_can_drive)
