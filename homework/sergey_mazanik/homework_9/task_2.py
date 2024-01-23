"""
Есть такой список:
temperatures =
[20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.
Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
"""

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

high_temperatures = list(filter(lambda i: i > 28, temperatures))
print(max(high_temperatures))
print(min(high_temperatures))
print(int(sum(high_temperatures) / len(high_temperatures)))


high_temperatures = list(map(lambda x: x if x > 28 else None, temperatures))
new_high = [temp for temp in high_temperatures if temp is not None]
print(max(new_high))
print(min(new_high))
print(int(sum(new_high) / len(new_high)))
