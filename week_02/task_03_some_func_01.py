# И всё таки придержусь snake_case и PEP8, вместо camelcase, потому чуток исправлю именовку функций
def my_first_function(a, b):
    return a + b
    # return a * b


def my_second_function(num):
    return num * num
    # return num ** 2


result = my_first_function(2, 2)
if result == 4:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = my_second_function(10)
if result == 100:
    print('Правильно :)')
else:
    print('Неправильно :(')
