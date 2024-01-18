"""
Создайте такую программу:
Программа хранит какую-либо цифру в переменной.
Программа просит пользователя угадать цифру. Пользователь вводит цифру.
Программа сравнивает цифру с той, что хранится в переменной.
Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
Т.е. программа не завершается пока пользователь не угадает цифру.
Подсказка: задание выполняется с помощью цикла while
"""

from random import randint


def is_numeric(string_number: str) -> bool:
    if string_number.isnumeric() and (0 < int(string_number) < 101):
        return True
    else:
        return False


num = randint(1, 100)
print(num)
while True:
    user_number = input('Write the number from 1 to 100: ')
    if is_numeric(user_number):
        if int(user_number) == num:
            print('Congratulations! You guessed it!')
            break
        else:
            print('Try again')
    else:
        print('You wrote wrong value!')
