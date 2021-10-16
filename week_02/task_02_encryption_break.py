public_key = 3403
prime_numbers = []
number = 1

while number < 100:
    count = 0
    i = 2
    half_number = number // 2

    while i <= half_number:
        if number % i == 0:
            count += 1
            # Тут стоит заострить внимание тем, кто построил логику на continue, для чего нам проверять число дальше,
            # если оно уже не подходит :) Тем самым мы сократим количество пробегов в цикле, сэкономим время и
            # увеличим производительность. Для сравнения, попробуйте добавить каунтер и увеличивать его каждый раз на
            # единицу сразу после написания начала цикла, а после исполнения все логики кода выведите
            # значение получившегося каунтера
            break
        i += 1

    if count == 0 and number != 1:
        prime_numbers.append(number)
    number += 1

for num in prime_numbers:
    if public_key % num == 0:
        # Можно по разному производить операцию деления, например, если хочется без остатка, можно юзать два слеша
        print(f"Prime numbers is: {num} and {public_key // num}")
        break
