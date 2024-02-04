import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query_1 = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
values = ('Zlatan', 'Ibrahimovic', 1)
cursor.execute(query_1, values)
student_id = cursor.lastrowid

query_2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Golden foot 21', student_id),
    ('The Best 12', student_id),
    ('Gold ball 32', student_id)
]
cursor.executemany(query_2, values)

query_3_1 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('test_sql_python_2', 'feb 01', 'in progress')
cursor.execute(query_3_1, values)
new_group_id = cursor.lastrowid

query_3_2 = "UPDATE students SET group_id = %s WHERE id = %s"
values = (new_group_id, student_id)
cursor.execute(query_3_2, values)

query_4_1 = "INSERT INTO subjets (title) VALUES (%s)"
values = ('Python for everyone 1st',)
cursor.execute(query_4_1, values)
first_subject_id = cursor.lastrowid
query_4_2 = "INSERT INTO subjets (title) VALUES (%s)"
values = ('Python for everyone 2st',)
cursor.execute(query_4_2, values)
second_subject_id = cursor.lastrowid

query_5_1 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = ('lesson_1', first_subject_id)
cursor.execute(query_5_1, values)
first_lesson_first_subject_id = cursor.lastrowid
query_5_2 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = ('lesson_2', first_subject_id)
cursor.execute(query_5_2, values)
second_lesson_first_subject_id = cursor.lastrowid
query_5_3 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = ('lesson_1', second_subject_id)
cursor.execute(query_5_3, values)
first_lesson_second_subject_id = cursor.lastrowid
query_5_4 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = ('lesson_2', second_subject_id)
cursor.execute(query_5_4, values)
second_lesson_second_subject_id = cursor.lastrowid

query_6_1 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (3, first_lesson_first_subject_id, student_id)
cursor.execute(query_6_1, values)
mark_first_lesson_first_subject_id = cursor.lastrowid
query_6_2 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (4, second_lesson_first_subject_id, student_id)
cursor.execute(query_6_2, values)
mark_second_lesson_first_subject_id = cursor.lastrowid
query_6_3 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (5, first_lesson_second_subject_id, student_id)
cursor.execute(query_6_3, values)
mark_first_lesson_second_subject_id = cursor.lastrowid
query_6_4 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (6, second_lesson_second_subject_id, student_id)
cursor.execute(query_6_4, values)
mark_second_lesson_second_subject_id = cursor.lastrowid

db.commit()

select_query_1 = '''
SELECT s.name, s.second_name, m.value
FROM students s
JOIN marks m
ON s.id = m.student_id
WHERE s.id = %s
'''
values = (student_id,)
cursor.execute(select_query_1, values)
data = cursor.fetchall()
print(data)
print()

select_query_2 = '''
SELECT s.name, s.second_name, b.title
FROM students s
JOIN books b
ON s.id = b.taken_by_student_id
WHERE s.id = %s
'''
values = (student_id,)
cursor.execute(select_query_2, values)
data = cursor.fetchall()
print(data)
print()

select_query_3 = '''
SELECT s.name AS student_name, s.second_name AS student_surname, b.title AS book_title, g.title AS group_title,
        g.start_date AS statr_course, g.end_date AS end_course, s2.title AS subject_title, l.title AS lesson_title,
        m.value AS mark
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
WHERE s.id = %s
'''
values = (student_id,)
cursor.execute(select_query_3, values)
data = cursor.fetchall()
print(data)

db.close()
