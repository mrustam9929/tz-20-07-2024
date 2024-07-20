import json
from dataclasses import dataclass
from enum import Enum, StrEnum

from exceptions import BookDoesNotExist


class BookStatus(StrEnum):
    AVAILABLE = 'в наличии'
    ISSUED = 'выдана'


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str


class BookManager:
    def __init__(self, books_file_path):
        self.books_file_path = books_file_path

    def create(self, title: str, author: str, year: int) -> Book:
        """
        Создание новой книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания
        :return: Book object
        """
        if books_keys := self.books.keys():
            book_id = max(books_keys) + 1
        else:
            book_id = 1
        book = Book(
            id=book_id,
            title=title,
            author=author,
            year=year,
            status=BookStatus.AVAILABLE
        )
        self.books[book_id] = book
        return book

    def delete(self, book_id: int) -> None:
        """
        Удаление книги
        :param book_id: id книги
        :return: None
        :except: BookDoesNotExist - если книги с таким id не существует
        """
        if not self.has_book_id(book_id):
            raise BookDoesNotExist(f'ID: {book_id} не существует')

        del self.books[book_id]

    def search(self, value: str) -> list:
        """
        Поиск книги по id
        :param value: str - Значение для поиска
        :return: список книг, удовлетворяющих поиску
        """
        result = []
        for book in self.books.values():
            if value == book.title or value == book.author or value == str(book.year):
                result.append(book)
        return result

    def all(self) -> list[Book]:
        """
        Получение всех книг
        :return: list[Book] - список всех книг
        """
        return list(self.books.values())

    def update_status(self, book_id: int, status: str) -> None:
        """
        Обновление статуса книги
        :param book_id:
        :param status: str ['available', 'unavailable'] - статус книги
        :return:
        """
        if not self.has_book_id(book_id):
            raise BookDoesNotExist(f'ID: {book_id} не существует')
        self.books[book_id].status = status

    def has_book_id(self, book_id: int) -> bool:
        """
        Проверка наличия книги
        :param book_id: int
        :return:
        """
        return book_id in self.books

    def __enter__(self) -> 'BookManager':
        """
        Чтение данных из файла
        :return: self
        """
        try:
            with open(self.books_file_path, 'r') as f:
                self.books = {book['id']: Book(**book) for book in json.load(f)}
        except FileNotFoundError or json.JSONDecodeError:
            self.books = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Запись данных в файл
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        with open(self.books_file_path, 'w') as f:
            json.dump([book.__dict__ for book in self.books.values()], f, indent=4)
