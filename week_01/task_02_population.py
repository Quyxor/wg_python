# По умолчанию sorted() сортирует от меньшего к большему
population_density = sorted([8.56, 3.5, 139, 32, 23.6, 2.8, 357])
# Вынесу в переменным длинну списка и сумму его значений, чтобы не пересчитывать их при переиспользовании
population_density_len = len(population_density)
population_density_sum = sum(population_density)

# Используем round() с точностью до одного знака после запятой
density_avg = round(population_density_sum/population_density_len, 1)
# Т.к. список со значениями начинается с наименьшего, то берем первый элемент
density_min_by_index = population_density[0]
# Или же, можем использовать встроенную функцию питона min()
density_min_by_min = min(population_density)
# Т.к. список со значениями начинается с наименьшего, то берем последний элемент
# Кстати, можно схитрить и взять отрицательный индекс, тогда будет браться последнее значение
density_max_by_index = population_density[-1]
# Или же, можем использовать встроенную функцию питона max()
density_max_by_max = max(population_density)
# Опять же, воспольуземся отрицательным индексом
density_top_three = population_density[-3:]

print(f"density_avg: {density_avg}")
print(f"density_min_by_index: {density_min_by_index}")
print(f"density_min_by_min: {density_min_by_min}")
print(f"density_max_by_index: {density_max_by_index}")
print(f"density_max_by_max: {density_max_by_max}")
print(f"density_top_three: {density_top_three}")

