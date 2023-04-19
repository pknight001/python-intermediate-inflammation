class Book:
    """A book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

    def __eq__(self, other):  # needed when comparing books, as in union function below
        return self.title == other.title and self.author == other.author

class Library:
    """A Library."""

    def __init__(self):
        self.books = []

    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def by_author(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(str(book))

        if len(books) == 0:
            raise KeyError('Author does not exist: ' + author)

        return books

    @property  # means we can exclude () when calling this function
    def titles(self):
        book_titles = []
        for book in self.books:
            book_titles.append(book.title)

        return book_titles

    @property
    def authors(self):
        book_authors = []
        for book in self.books:
            if book.author not in book_authors:
                book_authors.append(book.author)

        return book_authors

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return books


#---------------------------------------------------------
library = Library()
library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

print(library.titles)
print(library.authors)


library1 = Library()
library1.add_book('My First Book', 'Alice')
library1.add_book('My Second Book', 'Alice')

library2 = Library()
library2.add_book('My Second Book', 'Alice')
library2.add_book('A Different Book', 'Bob')

books = library1.union(library2)
for book in books:
    print(book)
