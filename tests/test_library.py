"""Tests for the Library and Book classes."""

import pytest

def test_createbook():
    from library import book

    title = 'My Book'
    author = 'Peter'
    b = book.Book(title, author)

    assert b.title == title
    assert b.author == author

def test_create_library():
    import library.library as library

    lib = library.Library()
    assert len(lib) == 0

def test_add_book_to_library():
    import library.library as library

    lib = library.Library()
    lib.add_book('MyBook', 'Alice')

    assert len(lib) == 1
    assert lib[0].title == 'MyBook'
    assert lib[0].author == 'Alice'

def test_by_author():
    import library.library as library

    lib = library.Library()
    lib.add_book('MyBook', 'Alice')
    lib.add_book('MyBook2', 'Alice')

    assert lib.by_author('Alice') == ['MyBook by Alice', 'MyBook2 by Alice']

def test_titles():
    import library.library as library

    lib = library.Library()
    lib.add_book('MyBook', 'Alice')
    lib.add_book('MyBook2', 'Alice')
    lib.add_book('MyBook', 'Bob')
    lib.add_book('BobsBook', 'Bob')

    assert lib.titles == ['MyBook', 'MyBook2', 'MyBook', 'BobsBook']

def test_authors():
    import library.library as library

    lib = library.Library()
    lib.add_book('MyBook', 'Alice')
    lib.add_book('MyBook2', 'Alice')
    lib.add_book('MyBook', 'Bob')
    lib.add_book('BobsBook', 'Bob')

    assert lib.authors == ['Alice', 'Bob']

