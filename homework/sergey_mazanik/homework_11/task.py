from abc import abstractmethod


class Book:
    pages_material = 'Paper'
    has_text = True

    def __init__(self, book_name, author, pages_count, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_info(self):
        if self.is_reserved:
            print(f'Name: {self.book_name}, Author: {self.author}, Pages: {self.pages_count}, '
                  f'Material: {self.pages_material}, Reserved')
        else:
            print(f'Name: {self.book_name}, Author: {self.author}, Pages: {self.pages_count}, '
                  f'Material: {self.pages_material}')

    def set_is_received(self, status_received: bool):
        self.is_reserved = status_received


class Textbook(Book):
    def __init__(self, book_name, author, pages_count, isbn, is_reserved, school_subject, class_number, has_tasks):
        super().__init__(book_name, author, pages_count, isbn, is_reserved)
        self.school_subject = school_subject
        self.class_number = class_number
        self.has_tasks = has_tasks

    def print_info_textbook(self):
        if self.is_reserved:
            print(f'Name: {self.book_name}, Author: {self.author}, Pages: {self.pages_count}, '
                  f'Subject: {self.school_subject}, Class: {self.class_number}, Reserved')
        else:
            print(f'Name: {self.book_name}, Author: {self.author}, Pages: {self.pages_count}, '
                  f'Subject: {self.school_subject}, Class: {self.class_number}')


first_book = Book("Harry Potter and the Sorcerer’s Stone", 'J.K.Rowling', 333,
                  '5-8451-0512-9', False)
second_book = Book("Harry Potter and the Chamber of Secrets", 'J.K.Rowling', 341,
                   '5-0439-06486-4', False)
third_book = Book("Harry Potter and the Prisoner of Azkaban", 'J.K.Rowling', 435,
                  '0-7475-4215-5', False)
forth_book = Book("Harry Potter and the Goblet of Fire", 'J.K.Rowling', 734,
                  '0-4391-3959-7', False)
fifth_book = Book("Harry Potter and the Order of the Phoenix", 'J.K.Rowling', 912,
                  '1-4088-5569-0', False)
first_textbook = Textbook('Math Makes Sense', 'Mike Czukar', 554, '0-3214-9558-6',
                          False, 'Math', 9, True)
second_textbook = Textbook('INFORMATION COMMUNICATION TECHNOLOGY', 'Dixit J.B.', 116,
                           '1-4919-3936-2', False, 'Information Technology',
                           11, True)

third_book.set_is_received(True)
second_textbook.set_is_received(True)

books = first_book, second_book, third_book, forth_book, fifth_book
textbooks = first_textbook, second_textbook

for book in books:
    book.print_info()

for textbook in textbooks:
    textbook.print_info_textbook()
