from enum import IntEnum

from manager import BookManager, BookStatus


class Action(IntEnum):
    CREATE = 1
    DELETE = 2
    SEARCH = 3
    ALL = 4
    UPDATE_STATUS = 5
    EXIT = 6


class ActionMethod:

    @staticmethod
    def create_book(manager: BookManager):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        while not year.isdigit():
            year = input("Введите корректный год издания книги: ")
        book = manager.create(title, author, int(year))
        print(f"Книга {book.title} успешно создана")

    @staticmethod
    def delete_book(manager: BookManager):
        book_id = input("Введите ID книги: ")
        while not book_id.isdigit() or not manager.has_book_id(int(book_id)):
            book_id = input("Введите корректный ID книги: ")
        manager.delete(int(book_id))
        print(f"Книга с ID {book_id} успешно удалена")

    @staticmethod
    def get_all_books(manager: BookManager):
        books = manager.all()
        if not books:
            print("Книги не найдены")
        else:
            for book in books:
                print(
                    f"ID: {book.id}, "
                    f"Название: {book.title}, "
                    f"Автор: {book.author}, "
                    f"Год: {book.year}, "
                    f"Cтатус: {book.status} \n"
                )

    @staticmethod
    def update_status(manager: BookManager):
        book_id = input("Введите ID книги: ")
        while not book_id.isdigit() or not manager.has_book_id(int(book_id)):
            book_id = input("Введите корректный ID книги: ")
        status = input("Введите статус книги: ")
        while status not in list(BookStatus):
            status = input("Введите корректный статус книги: ")
        manager.update_status(int(book_id), status)

    @staticmethod
    def search_book(manager: BookManager):
        search_value = input("Введите значение для поиска: ")
        books = manager.search(search_value)
        if not books:
            print("Книги не найдены")
        else:
            for book in books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year} \n")


def show_action_list():
    print("Добро пожаловать в библиотеку!")
    print(f"{Action.CREATE}. Создать книгу")
    print(f"{Action.DELETE}. Удалить книгу")
    print(f"{Action.SEARCH}. Поиск книги")
    print(f"{Action.ALL}. Вывести все книги")
    print(f"{Action.UPDATE_STATUS}. Обновить статус книги")


def get_action() -> int:
    value = input("Выберите действие: ")
    while not value.isdigit() or int(value) not in list(Action):
        value = input("Пожалуйста выберите действие из списка: ")
    return int(value)
