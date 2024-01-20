"""
Напишите функцию-генератор, которая генерирует список чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
"""


def fibonacci(limit=10):
    current_num = 1
    prev_num = 1
    count = 1
    while count < limit:
        yield current_num
        current_num, prev_num = prev_num, current_num + prev_num
        count += 1


def print_fibonacci(num):
    count = 1
    if num == 0:
        print(0)
    else:
        for number in fibonacci(1000000):
            if count == num:
                print(number)
                break
            count += 1


print_fibonacci(5)
print_fibonacci(200)
print_fibonacci(1000)
print_fibonacci(100000)  # тут будет ошибка, потому что количество символов превышает 4300
# print_fibonacci(20577)  # последнее число, доступное для вывода в Python
