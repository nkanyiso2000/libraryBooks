import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, title, author, publishDate):
        self.title = title
        self.author = author
        self.publishDate = publishDate
        self.borrowed = 0

    def borrow_book(self):
        if self.publishDate > self.borrowed:
            self.borrowed += 1
            return f'You have borrowed "{self.title}" by {self.author}'
        else:
            return f'Sorry, all copies of "{self.title}" are currently borrowed.'

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
            return f'You have returned "{self.title}" by {self.author}'
        else:
            return f'No copies of "{self.title}" are currently borrowed.'

    def __str__(self):
        return f'{self.title} by {self.author} (Available: {self.publishDate - self.borrowed}, Borrowed: {self.borrowed})'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publishDate):
        book = Book(title, author, publishDate)
        self.books.append(book)
        return f'Added "{title}" by {author} to the library.'

    def display_books(self):
        if not self.books:
            return "No books available in the library."
        else:
            return "\n".join(str(book) for book in self.books)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow_book()
        return f'Book titled "{title}" not found in the library.'

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f'Book titled "{title}" not found in the library.'

    def search_book(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not found_books:
            return f'No books found for "{keyword}".'
        else:
            return "\n".join(str(book) for book in found_books)


class LibraryApp:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")

        # Setup GUI elements
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Library Management System", font=("Arial", 16)).pack(pady=10)

        self.text_area = tk.Text(self.root, height=15, width=50)
        self.text_area.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Book", command=self.add_book).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Display All Books", command=self.display_books).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Borrow Book", command=self.borrow_book).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Return Book", command=self.return_book).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Search for a Book", command=self.search_book).grid(row=0, column=4, padx=5)

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter the title of the book:")
        author = simpledialog.askstring("Input", "Enter the author of the book:")
        publishDate = simpledialog.askinteger("Input", "Enter the Publish Date:")
        if title and author and publishDate is not None:
            result = self.library.add_book(title, author, publishDate)
            self.show_message(result)
        else:
            self.show_message("Invalid input, please try again.")

    def display_books(self):
        result = self.library.display_books()
        self.show_message(result)

    def borrow_book(self):
        title = simpledialog.askstring("Input", "Enter the title of the book to borrow:")
        if title:
            result = self.library.borrow_book(title)
            self.show_message(result)
        else:
            self.show_message("Invalid input, please try again.")

    def return_book(self):
        title = simpledialog.askstring("Input", "Enter the title of the book to return:")
        if title:
            result = self.library.return_book(title)
            self.show_message(result)
        else:
            self.show_message("Invalid input, please try again.")

    def search_book(self):
        keyword = simpledialog.askstring("Input", "Enter the title or author to search:")
        if keyword:
            result = self.library.search_book(keyword)
            self.show_message(result)
        else:
            self.show_message("Invalid input, please try again.")

    def show_message(self, message):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
