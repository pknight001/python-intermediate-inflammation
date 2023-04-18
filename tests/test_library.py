"""Tests for the Library and Book classes."""

import pytest

def test_createbook():
    from library import book

    title = 'My Book'
    author = 'Peter'
    b = book.Book(title, author)

    assert b.title == title
    assert b.author == author