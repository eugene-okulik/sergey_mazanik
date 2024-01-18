"""
Дан такой словарь:
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
III
lovelovelovelove
итд
Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)
Помните, что копипаст одного и того же кода - плохо
"""


def display_key_value_times(my_dict: dict):
    for key, value in my_dict.items():
        print(key * value)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
display_key_value_times(words)
