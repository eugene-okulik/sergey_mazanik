'''
Задание 3
Даны такие списки:
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
'''

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Первый вариант:
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))

# Второй вариант:
print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
