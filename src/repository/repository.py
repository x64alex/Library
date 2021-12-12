from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.module.module import DataStructure
import os
from datetime import date
import unittest
import pickle


class BookFunctions:
    """
    Class for functions related to book
    """

    def __init__(self):
        self.books = DataStructure(self.generate_books())

    def generate_books(self):
        """

        :return: the generated list of books
        :rtype: list
        """
        books_list = []

        authors = ['Joanne Rowling', 'Joanne Rowling', 'Joanne Rowling', 'Joanne Rowling', 'Joanne Rowling',
                   'Joanne Rowling', 'Joanne Rowling', 'Joanne Rowling', 'Joanne Rowling',
                   'Tolkien']
        books = ['Harry Potter 1', 'Harry Potter 2', 'Harry Potter 3', 'Harry Potter 4', 'Harry Potter 5',
                 'Harry Potter 6', 'Harry Potter 7', 'The Casual Vacancy', 'The Tales of the Bard',
                 'The Hobbit']
        for i in range(10):
            isbn = str(i)
            author = str(authors[i])
            title = str(books[i])

            books_list.append(Book(isbn, title, author))

        return books_list

    def return_book_id(self, id1):
        """

        :param id1: given id
        :return: The book with the given id
        """
        for bk in self.books.get_list:
            if bk.id == id1:
                return bk

    def check_book_id(self, book_id):
        for bk in self.books.get_list:
            if bk.id == book_id:
                return False
        return True

    def add_book(self, book):
        """
        Add the new book to the books list
        :param book: the new book from the console
        :return: nothing
        """
        if self.check_book_id(book.id):
            self.books.append(book)
        else:
            print("Bad book input!")

    def remove_book(self, book_id):
        """
        Remove the book with the given id from the list of books
        :param book_id: the given book id
        :return:
        """
        for bk in self.books.get_list:
            if bk.id == book_id:
                self.books.pop(self.books.index(bk))

    def update_book(self, book_id, title, author):
        """
        Update the book with the given id with the new title and new author
        :param book_id: given id
        :param title: new title
        :param author: new author
        :return:
        """
        for bk in self.books:
            if bk.id == book_id:
                bk.title = title
                bk.author = author

    def search_book(self, val):
        """

        :param val: input from user
        :return: list of clients
        """
        list_books = []
        value = val.lower()

        for book in self.books.get_list:
            id1 = book.id
            title = book.title.lower()
            author = book.author.lower()

            if id1.find(value) != -1 or title.find(value) != -1 or author.find(value) != -1:
                list_books.append(book)

        return list_books


class BookFunctionsBin(BookFunctions):
    def __init__(self, file):
        super().__init__()

        self._file_name = file
        self.books = []
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        if os.path.getsize(self._file_name) != 0:
            self.books = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self.books, f)
        f.close()

    def add_book(self, book):
        """
        1. Do whatever the add method in the base class does
        2. Save the ingredients to file
        """
        super(BookFunctionsBin, self).add_book(book)
        # super().add(entity)
        self._save_file()

    def remove_book(self, book_id):
        super(BookFunctionsBin, self).remove_book(book_id)

        self._save_file()

    def update_book(self, book_id, title, author):
        super(BookFunctionsBin, self).update_book(book_id, title, author)

        self._save_file()


class BookFunctionsTextFile(BookFunctions):
    def __init__(self, file):
        super().__init__()

        self._file_name = file
        self.books = []
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            book_id, title, author = line.split(maxsplit=2, sep=',')
            author = author[:-1]
            self.add_book(Book(book_id, title, author))
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode

        for book in self.books:
            f.write(str(book.id) + ',' + book.title + ',' + book.author)
            f.write('\n')
        f.close()

    def add_book(self, book):
        """
        1. Do whatever the add method in the base class does
        2. Save the ingredients to file
        """
        super(BookFunctionsTextFile, self).add_book(book)
        # super().add(entity)
        self._save_file()

    def remove_book(self, book_id):
        super(BookFunctionsTextFile, self).remove_book(book_id)

        self._save_file()

    def update_book(self, book_id, title, author):
        super(BookFunctionsTextFile, self).update_book(book_id, title, author)

        self._save_file()


class ClientFunctions:
    """
    Class for functions related to Client
    """

    def __init__(self):
        self.clients = DataStructure(self.generate_clients())

    def generate_clients(self):
        """
        :return: The generated list of clients
        """

        clients = []
        names = ['Joe', 'Phil', 'John', 'John McAfee', 'Darius', 'Luis McJohn', 'Joe', 'Phil', 'John', 'John McAfee',
                 'Darius', 'Luis McJohn', 'Joe', 'Phil', 'John', 'John McAfee', 'Darius', 'Luis McJohn']
        for i in range(10):
            isbn = str(i)
            name = str(names[i])

            clients.append(Client(isbn, name))

        return clients

    def check_client_id(self, client_id):
        """
        Check if the given id is already in the list
        :param client_id: given id
        :return: True if it is not False if it is
        """
        for cl in self.clients.get_list:
            if cl.id == client_id:
                return False
        return True

    def add_client(self, client):
        """
        Add new client to the list of clients
        :param client: new client
        :return:
        """
        if self.check_client_id(client):
            self.clients.append(client)

    def return_client_id(self, id1):
        """

        :param id1: given id
        :return: The client with the given id
        """
        for cl in self.clients.get_list:
            if cl.id == id1:
                return cl

    def remove_client(self, client_id):
        """
        Remove the client with the given id from the list
        :param client_id: given id
        :return:
        """
        client = self.return_client_id(client_id)
        if client is not None:
            self.clients.pop(self.clients.index(client))

    def update_client(self, client_id, name):
        """
        Update the book with the given id with the new name
        :param client_id: given id
        :param name: new name
        :return:
        """
        client = self.return_client_id(client_id)
        if client is not None:
            client.name = name

    def search_clients(self, val):

        """
        :param val: input from user
        :return:
        """
        list_clients = []
        value = val.lower()

        for client in self.clients.get_list:
            id1 = client.id
            name = client.name.lower()

            if id1.find(value) != -1 or name.find(value) != -1:
                list_clients.append(client)

        return list_clients


class ClientFunctionsTextFile(ClientFunctions):
    def __init__(self, file):
        super().__init__()

        self._file_name = file
        self.clients = []
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            client_id, name = line.split(maxsplit=2, sep=',')
            name = name[:-1]
            self.add_client(Client(client_id, name))

        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode

        for client in self.clients:
            f.write(str(client.id) + ',' + client.name + "\n")

        f.close()

    def add_client(self, client):
        super(ClientFunctionsTextFile, self).add_client(client)

        self._save_file()

    def remove_client(self, client_id):
        super(ClientFunctionsTextFile, self).remove_client(client_id)

        self._save_file()

    def update_book(self, client_id, name):
        super(ClientFunctionsTextFile, self).update_client(client_id, name)

        self._save_file()


class ClientFunctionsBin(ClientFunctions):
    def __init__(self, file):
        super().__init__()
        self.clients = []
        self._file_name = file
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        if os.path.getsize(self._file_name) != 0:
            self.clients = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self.clients, f)
        f.close()

    def add_client(self, client):
        super(ClientFunctionsBin, self).add_client(client)

        self._save_file()

    def remove_client(self, client_id):
        super(ClientFunctionsBin, self).remove_client(client_id)

        self._save_file()

    def update_book(self, client_id, name):
        super(ClientFunctionsBin, self).update_client(client_id, name)

        self._save_file()


class RentalFunctions:
    """
    Class for functions related to Rental
    """

    def __init__(self):
        self.rentals = DataStructure([])

    def print_rentals(self):
        for rent in self.rentals.get_list:
            print(rent)

    def last_rented_book(self, book_id, client_id):
        rent = Rental
        for rental in self.rentals.get_list:
            if rental.book_id == book_id and rental.client_id == client_id:
                rent = rental
        return rent

    def time_str(self):
        date_now = date.today()
        time = str(date_now.year) + '/' + str(date_now.month) + '/' + str(date_now.day)
        return time

    def rent(self, book, client_id):
        book.state = 0
        time = self.time_str()
        rent = Rental(len(self.rentals), book, client_id, time)
        # print(rent)
        self.rentals.append(rent)

    def returned(self, book, client_id):
        book.state = 1
        time = self.time_str()
        rent = self.last_rented_book(book.id, client_id)
        rent.returned = time
        # print(rent)

    def create_rent(self, rental_id, book, client_id, rented_date, returned_date="not returned"):
        rent = Rental(rental_id, book, client_id, rented_date, returned_date)
        self.rentals.append(rent)

    def rent_delete(self, book, client_id):
        rental = self.last_rented_book(book.id, client_id)

        for rent in self.rentals.get_list:
            if rent == rental:
                rental.book.state = 1
                self.rentals.pop()

    def returned_delete(self, book, client_id):
        rental = self.last_rented_book(book.id, client_id)

        self.rent_delete(book, client_id)
        book.state = 0
        rent = Rental(rental.rental_id, rental.book, rental.client_id, rental.rented)
        self.rentals.append(rent)


class RentalFunctionsTextFile(RentalFunctions):
    def __init__(self, file):
        super().__init__()

        self._file_name = file
        self.rentals = []
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            rental_id, book_id, book_title, book_author, client_id, rented_date, returned_date = line.split(maxsplit=8,
                                                                                                            sep=',')
            book = Book(book_id, book_title, book_author)
            returned_date = returned_date[:-1]
            self.create_rent(rental_id, book, client_id, rented_date, returned_date)

            f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode

        for rental in self.rentals:
            f.write(str(rental.rental_id) + ',' + str(rental.book_id) + ',' + str(rental.book.title) + ',' + str(
                rental.book.author) + ',' + str(rental.client_id) + ',' + str(
                rental.rented) + ',' + str(rental.returned) + "\n")

        f.close()

    def rent(self, book, client_id):
        super(RentalFunctionsTextFile, self).rent(book, client_id)

        self._save_file()

    def returned(self, book, client_id):
        super(RentalFunctionsTextFile, self).returned(book, client_id)

        self._save_file()

    def rent_delete(self, book, client_id):
        super(RentalFunctionsTextFile, self).rent_delete(book, client_id)

        self._save_file()

    def returned_delete(self, book, client_id):
        super(RentalFunctionsTextFile, self).returned_delete(book, client_id)

        self._save_file()


class RentalFunctionsBin(RentalFunctions):
    def __init__(self, file):
        super().__init__()

        self._file_name = file
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        if os.path.getsize(self._file_name) != 0:
            self.rentals = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self.rentals, f)
        f.close()

    def rent(self, book, client_id):
        super(RentalFunctionsBin, self).rent(book, client_id)

        self._save_file()

    def returned(self, book, client_id):
        super(RentalFunctionsBin, self).returned(book, client_id)

        self._save_file()

    def rent_delete(self, book, client_id):
        super(RentalFunctionsBin, self).rent_delete(book, client_id)

        self._save_file()

    def returned_delete(self, book, client_id):
        super(RentalFunctionsBin, self).returned_delete(book, client_id)

        self._save_file()


class Tests(unittest.TestCase):
    """
        This function is called before any test cases.
        We can add initialization code common to all methods here
            (e.g. reading an input file)
    """

    def setUp(self):
        unittest.TestCase.setUp(self)

    """
        This function is called after all test function are executed
        It's like the opposite of setUp, here you dismantle the test scaffolding
    """

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_books(self):
        func_book = BookFunctions()
        assert len(func_book.books) == 10

        book = Book(12, '12', '13')
        func_book.add_book(book)
        assert len(func_book.books) == 11
        assert func_book.books[10].title == '12'
        assert func_book.books[10].author == '13'

        func_book.remove_book(12)
        assert len(func_book.books) == 10

        func_book.update_book(0, '9', '9')
        assert len(func_book.books) == 10

    def test_clients(self):
        func_client = ClientFunctions()
        func_client.generate_clients()
        assert len(func_client.clients) == 10

        client = Client(12, '12')
        func_client.add_client(client)
        assert len(func_client.clients) == 11
        assert func_client.clients[10].name == '12'

        func_client.remove_client(12)
        assert len(func_client.clients) == 10

        func_client.update_client(0, 'Alex')
        assert len(func_client.clients) == 10


class RepositoryException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass
