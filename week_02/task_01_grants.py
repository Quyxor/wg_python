from students import students

# Использую списки, исходя из условий задачи, а также не вижу смысла создавать полкупии словаря, который у нас есть
# под рукой, в списки буду складывать только ID студентов, т.к. они уникальны, в дальнейшем при необходимости достать
# какую-либо информацию, смогу использовать список с ID для обращения к словарю по ключу
deduction_list        = []
grants_list           = []
increased_grants_list = []
regular_list          = []

for key, value in students.items():
    # Задам сразу переменные и единожды вытащу необходимые мне значения, избегаю излишних вычислений/операций
    attendance = value['посещаемость']
    grades = value['оценки'].values()
    average_grade = sum(grades)/len(grades)

    if average_grade <= 3.5 and attendance <= 0.7:
        deduction_list.append(key)
    # В таких случаях лучше оставлять комментарий, т.к. логика порядка условий не очевидна и последущие люди могут
    # совершить ошибку, не уловив этого скрытого смысла. Условие вынесено сюда, т.к. следующее условие не дало бы ему
    # выполниться в случае смены их порядка
    elif average_grade == 5 and attendance == 1:
        increased_grants_list.append(key)
    elif average_grade >= 4 and attendance >= 0.9:
        grants_list.append(key)
    else:
        regular_list.append(key)

print(f"\nDeduction list:")
for student in deduction_list:
    print(students[student]['ФИО'])

print(f"\nGrants list:")
for student in grants_list:
    print(students[student]['ФИО'])

print(f"\nIncreased grants list:")
for student in increased_grants_list:
    print(students[student]['ФИО'])

print(f"\nRegular list:")
for student in regular_list:
    print(students[student]['ФИО'])
