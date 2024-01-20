"""
Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.
Если bonus - true, то к salary должен быть добавлен рандомный бонус.
Примеры результатов:
10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'
"""

from random import random

bonus_percentage = round(random(), 2)
while True:
    salary = input('Write salary: ')
    if salary.isnumeric():
        salary = int(salary)
        bonus = input('Write "y" to turn bonus on or another key to turn bonus off : ')
        bonus_switcher = False
        if 'y' in bonus.lower():
            bonus_switcher = True
        if bonus_switcher:
            print(f'${int(salary + salary * bonus_percentage)}')
            break
        else:
            print(f'${salary}')
            break
    else:
        print('Please write the salary in numbers!\n')
