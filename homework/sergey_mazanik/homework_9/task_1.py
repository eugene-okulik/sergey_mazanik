"""
Дана такая дата: "Jan 15, 2023 - 12:05:33"
Преобразуйте эту дату в питоновский формат, после этого:
1. Распечатайте полное название месяца из этой даты
2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
"""
from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"

parse_date = datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
month_for_human = parse_date.strftime('%B')
full_date_for_human = parse_date.strftime('%d.%m.%Y, %H:%M')

print(month_for_human)
print(full_date_for_human)
