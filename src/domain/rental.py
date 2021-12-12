from src.domain.book import Book


class Rental:
    def __init__(self, rental_id, book, client_id, rented_date='not rented', returned_date='not returned'):
        """
        Create a new rental

        :param rental_id:
        :param book_id:
        :param client_id:
        :param rented_date:
        :param returned_date:
        """
        self._rental_id = rental_id
        self._book = book
        self._client_id = client_id
        self._rented_date = rented_date
        self._returned_date = returned_date

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def book_id(self):
        return self._book.id

    @property
    def book(self):
        return self._book

    @property
    def client_id(self):
        return self._client_id

    @property
    def rented(self):
        return self._rented_date

    @property
    def returned(self):
        return self._returned_date

    @returned.setter
    def returned(self, returned_date):
        self._returned_date = returned_date

    def __str__(self):
        return "Rental id: " + str(
            self.rental_id) + " Book id: " + self.book_id + " Client id: " + self.client_id + " Rented date: " + self._rented_date + " Returned date: " + self._returned_date


def test_rental():
    rental = Rental(1, Book(1, 1, 1), 1, '1')
    assert rental.rental_id == 1
    assert rental.book_id == 1
    assert rental.client_id == 1
    assert type(rental.book) == Book
    assert rental.rented == '1'
    assert rental.returned == 'not returned'
    rental.returned = '1'
    assert rental.returned == '1'


test_rental()
