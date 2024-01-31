--Создайте в базе данных полный набор информации о студенте, заполнив все таблички:

--1. Создайте студента (student)

INSERT INTO students (name, second_name, group_id) VALUES ('Jhon', 'Snow', 1)
UPDATE students SET name = 'John', group_id = 184 WHERE id = 221 -- исправил имя и айди группы у студента на правильные

--2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

INSERT INTO books (title, taken_by_student_id) VALUES ('Harry Potter', 221)
INSERT INTO books (title, taken_by_student_id) VALUES ('Python', 221)
INSERT INTO books (title, taken_by_student_id) VALUES ('How to start AQA', 221)

--3. Создайте группу (group) и определите своего студента туда

INSERT INTO `groups` (title, start_date, end_date) VALUES ('sergey_test', 'jan 31', 'in progress')

--4. Создайте несколько учебных предметов (subjects)

INSERT INTO subjets (title) VALUES ('Python for everyone')
INSERT INTO subjets (title) VALUES ('Start of SQL')

--5. Создайте по два занятия для каждого предмета (lessons)

INSERT INTO lessons (title, subject_id) VALUES ('lesson_1', 238)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_2', 238)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_1', 239)
INSERT INTO lessons (title, subject_id) VALUES ('lesson_2', 239)

--6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 278, 221)
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 279, 221)
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 280, 221)
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 281, 221)

--Получите информацию из базы данных:

--1. Все оценки студента

SELECT s.name, s.second_name, m.value
FROM students s
JOIN marks m
ON s.id = m.student_id
WHERE s.id = 221

--2. Все книги, которые находятся у студента

SELECT s.name, s.second_name, b.title
FROM students s
JOIN books b
ON s.id = b.taken_by_student_id
WHERE s.id = 221

--3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
--(всё одним запросом с использованием Join)

SELECT s.name AS student_name, s.second_name AS student_surname,
	b.title AS book_title, g.title AS group_title,
	g.start_date AS statr_course, g.end_date AS end_course,
	s2.title AS subject_title, l.title AS lesson_title, m.value AS mark
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
WHERE s.id = 221
