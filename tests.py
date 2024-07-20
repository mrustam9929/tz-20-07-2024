import os
from unittest import TestCase
from manager import BookManager

from manager import BookStatus


class Test(TestCase):

    def test_create_book(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Test Author', 2000)
            self.assertEqual(book.title, 'Test')
            self.assertEqual(book.author, 'Test Author')
            self.assertEqual(book.year, 2000)
            self.assertEqual(book.status, BookStatus.AVAILABLE)
            self.assertEqual(book.id, 1)

    def test_delete_book(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Test Author', 2000)
            self.assertEqual(len(manager.all()), 1)
            manager.delete(book.id)
            self.assertEqual(len(manager.all()), 0)

    def test_search_book(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Author', 2000)
            self.assertEqual(manager.search('Test'), [book])
            self.assertEqual(manager.search('Author'), [book])
            self.assertEqual(manager.search('2000'), [book])

    def test_update_status(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Author', 2000)
            self.assertEqual(book.status, BookStatus.AVAILABLE)

            manager.update_status(book.id, BookStatus.ISSUED)
            self.assertEqual(book.status, BookStatus.ISSUED)

            manager.update_status(book.id, BookStatus.AVAILABLE)
            self.assertEqual(book.status, BookStatus.AVAILABLE)

    def test_all_books(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Author', 2000)
            self.assertEqual(manager.all(), [book])

    def test_has_book_id(self):
        self.delete_test_books_file()
        with BookManager('test_books.json') as manager:
            book = manager.create('Test', 'Author', 2000)
            self.assertTrue(manager.has_book_id(book.id))
            self.assertFalse(manager.has_book_id(789789798))

    @staticmethod
    def delete_test_books_file():
        try:
            os.remove('test_books.json')
        except FileNotFoundError:
            pass
