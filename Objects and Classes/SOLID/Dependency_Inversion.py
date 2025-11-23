from abc import ABC, abstractmethod

class Book:
    def __init__(self, content: str):
        self.content = content

class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class PlainTextFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content

class HTMLFormatter(Formatter):
    def format(self, book: Book) -> str:
        return f"<html><body>{book.content}</body></html>"

class MarkdownFormatter(Formatter):
    def format(self, book: Book) -> str:
        return f"**{book.content}**"
class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def print_book(self, book: Book):
        return self.formatter.format(book)

book = Book("Hello world")

printer1 = Printer(PlainTextFormatter())
print(printer1.print_book(book))   # Hello world

printer2 = Printer(HTMLFormatter())
print(printer2.print_book(book))   # <html>...

printer3 = Printer(MarkdownFormatter())
print(printer3.print_book(book))   # **Hello world**
