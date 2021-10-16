# И всё таки придержусь snake_case и PEP8, вместо camelcase, потому чуток исправлю именовку функций
def my_first_function(*nums):
    return sum(nums)


def my_second_function(*nums):
    res = 1

    for num in nums:
        res *= num

    return res


result = my_first_function(2)
if result == 2:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_first_function(2, 4)
if result == 6:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_first_function(5, 10, 15)
if result == 30:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function(5)
if result == 5:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function(5, 5)
if result == 25:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function(10, 9, 2)
if result == 180:
    print('Правильно :)')
else:
    print('Неправильно :(')
