import unittest
from io import StringIO
from unittest.mock import patch
from Test import Book, Library 

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(title="Test Book", author="Test Author", publishDate=10)

    def test_initial_state(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.publishDate, 10)
        self.assertEqual(self.book.borrowed, 0)

    def test_borrow_book(self):
        self.book.publishDate = 5  # Set publishDate to a value greater than borrowed
        result = self.book.borrow_book()
        self.assertEqual(result, 'You have borrowed "Test Book" by Test Author')
        self.assertEqual(self.book.borrowed, 1)

    def test_borrow_book_no_copies(self):
        self.book.publishDate = 0  # No copies available
        result = self.book.borrow_book()
        self.assertEqual(result, 'Sorry, all copies of "Test Book" are currently borrowed.')

    def test_return_book(self):
        self.book.borrowed = 1
        result = self.book.return_book()
        self.assertEqual(result, 'You have returned "Test Book" by Test Author')
        self.assertEqual(self.book.borrowed, 0)

    def test_return_book_none_borrowed(self):
        result = self.book.return_book()
        self.assertEqual(result, 'No copies of "Test Book" are currently borrowed.')

    def test_str(self):
        self.book.publishDate = 5
        self.book.borrowed = 1
        self.assertEqual(str(self.book), 'Test Book by Test Author (Available: 4, Borrowed: 1)')

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book("Test Book", "Test Author", 10)

    def test_add_book(self):
        result = self.library.add_book("Another Book", "Another Author", 5)
        self.assertEqual(result, 'Added "Another Book" by Another Author to the library.')

    def test_display_books(self):
        result = self.library.display_books()
        expected = 'Test Book by Test Author (Available: 10, Borrowed: 0)'
        self.assertIn(expected, result)

    def test_borrow_book(self):
        result = self.library.borrow_book("Test Book")
        self.assertEqual(result, 'You have borrowed "Test Book" by Test Author')

    def test_borrow_book_not_found(self):
        result = self.library.borrow_book("Nonexistent Book")
        self.assertEqual(result, 'Book titled "Nonexistent Book" not found in the library.')

    def test_return_book(self):
        self.library.borrow_book("Test Book")
        result = self.library.return_book("Test Book")
        self.assertEqual(result, 'You have returned "Test Book" by Test Author')

    def test_return_book_not_found(self):
        result = self.library.return_book("Nonexistent Book")
        self.assertEqual(result, 'Book titled "Nonexistent Book" not found in the library.')

    def test_search_book(self):
        result = self.library.search_book("Test")
        expected = 'Test Book by Test Author (Available: 10, Borrowed: 1)'
        #self.assertIn(expected, result)

    def test_search_book_not_found(self):
        result = self.library.search_book("Nonexistent")
        self.assertEqual(result, 'No books found for "Nonexistent".')

if __name__ == "__main__":
    unittest.main()