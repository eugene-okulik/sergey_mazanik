import mysql.connector as mysql
import os
import dotenv
import collections
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
current_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(current_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data_csv = []
    for row in file_data:
        data_csv.append(row)

select_query = f'''
SELECT s.name AS name, s.second_name AS second_name, g.title AS group_title, b.title AS book_title,
        s2.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
FROM students s
JOIN books b
ON s.id = b.taken_by_student_id
JOIN `groups` g
ON s.group_id = g.id
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON m.lesson_id = l.id
JOIN subjets s2
ON l.subject_id  = s2.id
'''
cursor.execute(select_query)
data_db = cursor.fetchall()

missed_data = [row for row in data_csv if row not in data_db]

print(*missed_data, sep='\n')
