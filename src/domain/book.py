class Book:

    def __init__(self, book_id, title, author):
        """
        Create a new book

        :param book_id:
        :param title:
        :param author:
        """
        self._book_id = book_id
        self._title = title
        self._author = author
        self._state = 1

    @property
    def id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author

    def __str__(self):
        return 'Book Id:' + str(self._book_id) + ' Title: ' + self._title + ' Author: ' + self._author


def test_book():
    book = Book(12, '31', '16')
    # print(book)
    assert book.id == 12
    assert book.title == '31'
    assert book.author == '16'
    assert book.state == 1
    book.title = '1'
    assert book.title == '1'
    book.state = '0'
    assert book.state == '0'
    book.author = '15'
    assert book.author == '15'
    assert str(book) == 'Book Id:12 Title: 1 Author: 15'



test_book()
