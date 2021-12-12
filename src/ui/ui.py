from src.domain.book import Book
from src.domain.client import Client


class RepositoryException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass


class UI:
    def __init__(self, undo_service, book_service, client_service, rental_service):
        self._undo_service = undo_service
        self._func_book = book_service
        self._func_client = client_service
        self._func_rental = rental_service

    def _show_menu(self):
        print("0. Exit")
        print("1. Add book")
        print("2. Remove book")
        print("3. Update book")
        print("4. List books")
        print("5. Add client")
        print("6. Remove client")
        print("7. Update client")
        print("8. List clients")
        print("9. Rent a book")
        print("10. Return a book")
        print("11. Search books")
        print("12. Search clients")
        print("13. Most rented books")
        print("14. Most active clients")
        print("15. Most rented author")
        print("16. Undo")
        print("17. Redo")
        print("18. Print rentals")

    """
    Book related ui functions
    """

    def _add_book_ui(self):
        book_id = input("Book id: ")
        title = input("Title: ")
        author = input("Author: ")
        book = Book(book_id, title, author)
        self._func_book.add_book(book)

    def _remove_book_ui(self):
        book_id = input("Book id: ")
        self._func_book.remove_book(book_id)

    def _update_book_ui(self):
        book_id = input("Book id: ")
        title = input("Title: ")
        author = input("Author: ")
        self._func_book.update_book(book_id, title, author)

    def _list_books(self):
        list_books = self._func_book.books.get_list()
        for book in list_books:
            print(book)

    """
    Client related ui functions
    """

    def _add_client_ui(self):
        client_id = input("Client id: ")
        name = input("Name: ")
        client = Client(client_id, name)
        self._func_client.add_clients(client)

    def _remove_client_ui(self):
        client_id = input("Client id: ")
        self._func_client.remove_client(client_id)

    def _update_client_ui(self):
        client_id = input("Client id: ")
        name = input("Name: ")
        self._func_client.update_client(client_id, name)

    def _list_clients(self):
        list_clients = self._func_client.clients.get_list()
        for client in list_clients:
            print(client)

    """
    Rent/Return Ui functions
    """

    def _rent_ui(self):
        book_id = input("Book id: ")
        book = self._func_book.func_books.return_book_id(book_id)
        if book == None:
            return
        if book.state == 1:
            client_id = input("Client id: ")

            if not self._func_client.func_clients.check_client_id(client_id):
                book.state = 0
                self._func_rental.rent(book, client_id)
            else:
                print("We do not have that client!")
        else:
            print("Book is already rented")

    def _return_ui(self):
        book_id = input("Book id: ")
        book = self._func_book.func_books.return_book_id(book_id)
        if type(book) != Book:
            raise RepositoryException("Bad value!")
        if book.state == 0:
            client_id = input("Client id: ")

            if not self._func_client.func_clients.check_client_id(client_id):
                if self._func_rental.func_rental.last_rented_book(book_id, client_id).client_id == client_id:
                    book.state = 1
                    self._func_rental.returned(book, client_id)
                else:
                    print("This client have not rented this book! ")
            else:
                print("We do not have that client!")
        else:
            print("Book is not rented")

    def print_rentals(self):
        self._func_rental.func_rental.print_rentals()

    """
    Search functions
    """

    def search_book(self):

        value = input("Name: ")
        books = self._func_book.search_book(value)
        for book in books:
            print(book)

    def search_client(self):
        value = input("Name: ")
        clients = self._func_client.search_clients(value)
        for client in clients:
            print(client)

    """
    Statistics
    """

    def most_rented_books(self):
        rented_books = self._func_book.most_rented_books()
        # print(rented_books)
        for rent in rented_books:
            print(rent[0])
            print("Number of rented times: " + str(rent[1]))

    def most_active_clients(self):
        active_clients = self._func_client.most_active_clients()
        for client in active_clients:
            print(client[0].name + ' has ' + str(client[1]) + ' rental days')

    def most_rented_author(self):
        rented_authors = self._func_book.most_rented_author()
        for rent in rented_authors:
            print('Author: ' + str(rent[0]) + ' Number of rentals: ' + str(rent[1]))

    """
    Undo/Redo
    """

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()

    """
    Start
    """

    def start(self):

        while True:
            self._show_menu()
            opt = input("")
            if opt == '0':
                return
            elif opt == '1':
                self._add_book_ui()
            elif opt == '2':
                self._remove_book_ui()
            elif opt == '3':
                self._update_book_ui()
            elif opt == '4':
                self._list_books()
            elif opt == '5':
                self._add_client_ui()
            elif opt == '6':
                self._remove_client_ui()
            elif opt == '7':
                self._update_client_ui()
            elif opt == '8':
                self._list_clients()
            elif opt == '9':
                self._rent_ui()
            elif opt == '10':
                self._return_ui()
            elif opt == '11':
                self.search_book()
            elif opt == '12':
                self.search_client()
            elif opt == '13':
                self.most_rented_books()
            elif opt == '14':
                self.most_active_clients()
            elif opt == '15':
                self.most_rented_author()
            elif opt == '16':
                self.undo()
            elif opt == '17':
                self.redo()
            elif opt == '18':
                self.print_rentals()
            else:
                print("Bad input")
