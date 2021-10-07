# Для красоты и удобочитаемости, при создании словаря, переносите его содержимое на новую строку
planets = {
    "Меркурий": 57910006,
    "Венера": 108199995,
    "Земля": 149599951,
    "Марс": 227939920,
    "Юпитер": 778330257,
    "Сатурн": 1429400028,
    "Уран": 2870989228,
    "Нептун": 4504299579,
}

# Немного о именовании в питоне, не стоит называть переменные кемелкейсом, начиная с большой буквы, аля DistToSunAvg
# Т.к. это правило названия классов в питоне, аля class MyClass(): - и многие интепритаторы будут ругаться на это
# Это не ошибка, но противоречит общепринятым стандартам - PEP8, вообще в питоне принято называть переменные через
# нижнее подчеркивание, аля dist_to_sun_avg, но в силу привычки/красоты могут использовать и кемелкейс,
# но не с большой буквы, аля distToSunAvg
dist_to_sun_avg = sum(list(planets.values())) / len(planets)
planets_names_sorted = sorted(list(planets.keys()))
farther_value = planets['Нептун'] / planets['Земля']

print(
    f"dist_to_sun_avg: {dist_to_sun_avg}, "
    f"planets_names_sorted: {planets_names_sorted}, "
    f"farther_value: {farther_value}"
)
