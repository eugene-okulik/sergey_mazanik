"""
Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами (числа и
операция передаются в аргументы функции). Функция выглядит примерно так:
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)
Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""


def decor_calc(func):
    def wrapper(num_1, num_2):
        if num_1 < 0 or num_2 < 0:
            return func(num_1, num_2, '*')
        else:
            if num_1 == num_2:
                return func(num_1, num_2, '+')
            elif num_1 > num_2:
                return func(num_1, num_2, '-')
            elif num_2 > num_1:
                return func(num_1, num_2, '/')

    return wrapper


@decor_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return 'division by zero'
        else:
            return first / second


first_number = int(input('Write first number here: '))
second_number = int(input('Write second number here: '))
print(calc(first_number, second_number))
