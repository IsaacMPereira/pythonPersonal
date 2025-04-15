class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [{f"{book.title} by {book.author}"} for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

lib1 = Library("lib1")

b1 = Book("t1", "au1")
b2 = Book("t2", "au2")
b3 = Book("t3", "au3")

lib1.add_book(b1)
lib1.add_book(b2)
lib1.add_book(b3)

for book in lib1.list_books():
    print(book)