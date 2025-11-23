class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_books(self):
        return self._books

class BookFinder:
    @staticmethod
    def find_by_title(books, title):
        return next((b for b in books if b.title == title), None)

book_1 = Book("The Creative Act", "Rick Rubin")
book_2 = Book("Half American", "Matthew F. Delmont")
book_3 = Book("The Lord of the Rings", "J.R.R. Tolkien")

library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)

result = BookFinder.find_by_title(library.list_books(), "The Creative Act")

print(result.title if result else "Book not found")
