# И всё таки придержусь snake_case и PEP8, вместо camelcase, потому чуток исправлю именовку функций
def my_first_function(a=2, b=2):
    return a + b


def my_second_function(value=10):
    return value * value
    # return value ** 2


result = my_first_function()
if result == 4:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_first_function(a=3)
if result == 5:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_first_function(b=1)
if result == 3:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function()
if result == 100:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function(value=20)
if result == 400:
    print('Правильно :)')
else:
    print('Неправильно :(')
