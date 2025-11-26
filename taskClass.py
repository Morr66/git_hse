"""
==============================================
  📚 ПРОЕКТ: СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ
==============================================
Цель:
Создать консольное приложение, моделирующее работу библиотеки
с использованием ООП-концепций: наследование, инкапсуляция,
полиморфизм и взаимодействие объектов.

----------------------------------------------
КЛАССЫ, КОТОРЫЕ НУЖНО РЕАЛИЗОВАТЬ:
----------------------------------------------

1. Класс Book (базовый)
   - Инкапсулированные атрибуты:
       __title, __author, __year, __available
   - Методы:
       get_title(), get_author(), get_year()
       is_available(), mark_as_taken(), mark_as_returned()
       __str__()

2. Класс PrintedBook(Book)
   - Дополнительные атрибуты:
       pages, condition ("новая", "хорошая", "плохая")
   - Методы:
       repair() — улучшает состояние книги

3. Класс EBook(Book)
   - Дополнительные атрибуты:
       file_size (МБ), format (pdf, epub, mobi)
   - Методы:
       download() — выводит сообщение о загрузке

4. Класс User
   - Атрибуты:
       name, __borrowed_books (инкапсулированный список)
   - Методы:
       borrow(book), return_book(book)
       show_books(), get_borrowed_books()

5. Класс Librarian(User) — наследник
   - Дополнительные методы:
       add_book(library, book)
       remove_book(library, title)
       register_user(library, user)

6. Класс Library
   - Инкапсулированные атрибуты:
       __books — список всех книг
       __users — список зарегистрированных пользователей
   - Методы:
       add_book(book), remove_book(title)
       add_user(user)
       find_book(title)
       show_all_books(), show_available_books()
       lend_book(title, user_name)
       return_book(title, user_name)

----------------------------------------------
ДОПОЛНИТЕЛЬНЫЕ ИДЕИ:
----------------------------------------------
- Ограничить количество книг у пользователя (не более 3)
- Добавить поиск по автору или году
- Реализовать сохранение данных в JSON
- Добавить класс AudioBook (наследник Book)
- Сделать меню (CLI) для управления библиотекой
----------------------------------------------
"""


class Book:
    def __init__(self, title, author, year, available = True):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_availavble(self):
        return self.__available

    def __str__(self):
        a = "доступна" if self.__available else "недоступна"
        return f"Название книги: {self.__title}, автор книги: {self.__author}, год книги: {self.__year}, книга {a}"

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition, available = True):
        super().__init__(title, author, year, available)
        self.__pages = pages
        self.__condition = condition



    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

class EBook(Book):
    def __init__(self,title, author, year,file_size,format, available = True):
        super().__init__(title,author,year,available)
        self.__file_size = file_size
        self.__format = format
    def download(self):
        print(f"Книга {self.get_title()}.{self.__format} размером {self.__file_size}МБ загружается...")


class User:
    def __init__(self,name):
        self.name = name
        self.__borrowed_books = []
    def borrow(self,Book):
        if Book.is_available():
            self.__borrowed_books.append(Book)
            print(f"Вы успешно взяли книгу {Book.get_title()}")
            Book.mark_as_taken()
        else:
            print(f"Книга {Book.__title} недоступна")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
    def add_book(self,Book):
        self.__books.append(Book)

    def remove_book(self, title):
        book_to_remove = self.find_book(title)
        if book_to_remove:
            self.__books.remove(book_to_remove)
            return True
        return False

    def add_user(self, user):
        self.__users.append(user)

    def find_book(self, title):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def show_all_books(self):
        if self.__books:
            print("Все книги в библиотеке:")
            for i, book in enumerate(self.__books, 1):
                print(f"  {i}. {book}")
        else:
            print("  Пока нет книг")
    def show_available_books(self):
        available_books = [book for book in self.__books if book.is_available()]
        if available_books:
            print("Доступные книги: ")
            for i, book in enumerate(available_books, 1):
                print(f"  {i}. {book}")
        else:
            print("Нет доступных книг")

    def lend_book(self, title, user_name):
        try:
            ft = self.find_book(title)
            fu = self.find_user(user_name)
            if not ft:
                print('Книга не найдена')
            elif not fu:
                print('Пользователь не найден')
            else:
                user_name.borrow(title)
                self.__book.pop(ft)

    def return_book(self,title,user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)
        if not book:
            print('Книга не найдена')
        elif not user:
            print('Пользователь не найден')
        else:
            user.return_book(book)
class Librarian(User):
    def add_book(self,library,book):
        library.add_book(book)
    def remove_book(self,library,book):
        library.remove_book(book)
    def register_user(self,library,user):
        library.add_user(user)




a = Book("Война и мир", "Толстой", 1869, 1)
print(a.is_availavble())
print(a)
b = PrintedBook("Война и мир", "Толстой", 1869, 0, 100,'хорошая')
print(b)
if __name__ == '__main__':
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, 300, "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)

    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    # --- пользователь смотрит свои книги ---
    user1.show_books()

    # --- возвращает книгу ---
    lib.return_book("Война и мир", "Анна")

    # --- электронная книга ---
    b2.download()

    # --- ремонт книги ---
    b3.repair()
    print(b3)
