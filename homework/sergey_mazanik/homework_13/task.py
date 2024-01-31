import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
current_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(file_path):
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file(current_file_path):
    try:
        date_time = data_line.split(' - ')
        line_number, full_date_time = date_time[0].split('. ')
        date = datetime.datetime.strptime(full_date_time, "%Y-%m-%d %H:%M:%S.%f")
        if line_number == '1':
            print(date + datetime.timedelta(days=7))
        elif line_number == '2':
            print(date.strftime('%A'))
        elif line_number == '3':
            print((datetime.datetime.now() - date).days)
    except ValueError:
        print('Homework done')
