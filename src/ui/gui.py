import tkinter as tk
from tkinter import ttk
from src.domain.book import Book
from src.domain.client import Client


class GUI:
    """
      Implement the graphic user interface for add/list students
    """

    def __init__(self, undo_service, book_service, client_service, rental_service):
        self.frame = None
        self._undo_service = undo_service
        self._func_book = book_service
        self._func_client = client_service
        self._func_rental = rental_service

    def print(self, text):

        root = tk.Tk()

        # place a label on the root window
        message = tk.Label(root, text=text)
        message.pack()

        # keep the window displaying
        root.mainloop()

    def print_list(self, list):
        root = tk.Tk()

        # place a label on the root window
        for text in list:
            message = tk.Label(root, text=text)
            message.pack()

        # keep the window displaying
        root.mainloop()

    """
    Book related ui functions
    """

    def _add_book_ui(self, book_id, title, author):
        book = Book(book_id, title, author)
        self._func_book.add_book(book)

    def _remove_book_ui(self, book_id):
        self._func_book.remove_book(book_id)

    def _update_book_ui(self, book_id, title, author):
        self._func_book.update_book(book_id, title, author)

    def _list_books(self):
        self.print_list(self._func_book.books.list)

    """
    Client related ui functions
    """

    def _add_client_ui(self, client_id, name):
        client = Client(client_id, name)
        self._func_client.add_clients(client)

    def _remove_client_ui(self, client_id):
        self._func_client.remove_client(client_id)

    def _update_client_ui(self, client_id, name):
        self._func_client.update_client(client_id, name)

    def _list_clients(self):
        self.print_list(self._func_client.clients.get_list)

    """
    Rent/Return Ui functions
    """

    def _rent_ui(self, book_id, client_id):
        book = self._func_book.func_books.return_book_id(book_id)

        if book.state == 1:

            if not self._func_client.func_clients.check_client_id(client_id):
                book.state = 0
                self._func_rental.rent(book, client_id)
            else:
                print("We do not have that client!")
        else:
            print("Book is already rented")

    def _return_ui(self, book_id, client_id):
        book = self._func_book.func_books.return_book_id(book_id)
        if type(book) != Book:
            print("Bad value!")
        if book.state == 0:

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

    def search_book(self, value):

        books = self._func_book.search_book(value)
        self.print_list(books)

    def search_client(self, value):
        clients = self._func_client.search_clients(value)
        self.print_list(clients)

    """
    Statistics
    """

    def most_rented_books(self):
        rented_books = self._func_book.most_rented_books()
        books = []
        for rent in rented_books:
            books.append(rent[0])
            books.append("Number of rented times: " + str(rent[1]))
        self.print_list(books)

    def most_active_clients(self):
        active_clients = self._func_client.most_active_clients()
        books = []
        for client in active_clients:
            books.append(client[0].name + ' has ' + str(client[1]) + ' rental days')
        self.print_list(books)

    def most_rented_author(self):
        rented_authors = self._func_book.most_rented_author()
        books = []
        for rent in rented_authors:
            books.append('Author: ' + str(rent[0]) + ' Number of rentals: ' + str(rent[1]))
        self.print_list(books)

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
        frame = tk.Tk()
        frame.geometry("700x700")
        frame.title('Library')
        frame.resizable(0, 0)

        lbl = ttk.Label(frame, text="Book id:")
        lbl.grid(column=0, row=0, padx=5, pady=5)

        book_add_id = ttk.Entry(frame, {})
        book_add_id.grid(column=1, row=0, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Title:")
        lbl.grid(column=2, row=0)

        book_add_title = ttk.Entry(frame, {})
        book_add_title.grid(column=3, row=0)

        lbl = ttk.Label(frame, text="Author:")
        lbl.grid(column=4, row=0)

        book_add_author = ttk.Entry(frame, {})
        book_add_author.grid(column=5, row=0, padx=5, pady=5)

        button = ttk.Button(frame, text="Add book",
                            command=lambda: self._add_book_ui(book_add_id.get(), book_add_title.get(),
                                                              book_add_author.get()))
        button.grid(row=0, column=6)

        lbl = ttk.Label(frame, text="Book id:")
        lbl.grid(column=0, row=1, padx=5, pady=5)

        book_remove_id = ttk.Entry(frame, {})
        book_remove_id.grid(column=1, row=1, padx=5, pady=5)

        button = ttk.Button(frame, text="Remove book",
                            command=lambda: self._remove_book_ui(book_remove_id.get()))
        button.grid(column=6, row=1, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Book id:")
        lbl.grid(column=0, row=2, padx=5, pady=5)

        book_update_id = ttk.Entry(frame, {})
        book_update_id.grid(column=1, row=2, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Title:")
        lbl.grid(column=2, row=2)

        book_update_title = ttk.Entry(frame, {})
        book_update_title.grid(column=3, row=2)

        lbl = ttk.Label(frame, text="Author:")
        lbl.grid(column=4, row=2)

        book_update_author = ttk.Entry(frame, {})
        book_update_author.grid(column=5, row=2, padx=5, pady=5)

        button = ttk.Button(frame, text="Update book",
                            command=lambda: self._update_book_ui(book_update_id.get(),
                                                                 book_update_title.get(),
                                                                 book_update_author.get()))
        button.grid(column=6, row=2, padx=0, pady=0)

        button = ttk.Button(frame, text="List books", command=lambda: self._list_books())
        button.grid(column=6, row=3, padx=5, pady=5)

        """
        Client buttons
        """
        lbl = ttk.Label(frame, text="Client id:")
        lbl.grid(column=0, row=4, padx=5, pady=5)

        client_add_id = ttk.Entry(frame, {})
        client_add_id.grid(column=1, row=4, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Name:")
        lbl.grid(column=2, row=4)

        client_add_name = ttk.Entry(frame, {})
        client_add_name.grid(column=3, row=4, padx=5, pady=5)

        button = ttk.Button(frame, text="Add client", command=lambda: self._add_client_ui(client_add_id.get(),
                                                                                          client_add_name.get()))
        button.grid(column=6, row=4, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Client id:")
        lbl.grid(column=0, row=5)

        client_remove_id = ttk.Entry(frame, {})
        client_remove_id.grid(column=1, row=5, padx=5, pady=5)

        button = ttk.Button(frame, text="Remove client", command=lambda: self._remove_client_ui(client_remove_id.get()))
        button.grid(column=6, row=5, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Client id:")
        lbl.grid(column=0, row=6, padx=5, pady=5)

        client_update_id = ttk.Entry(frame, {})
        client_update_id.grid(column=1, row=6, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Name:")
        lbl.grid(column=2, row=6)

        client_update_name = ttk.Entry(frame, {})
        client_update_name.grid(column=3, row=6, padx=5, pady=5)

        button = ttk.Button(frame, text="Update client",
                            command=lambda: self._update_client_ui(client_update_id.get(), client_update_name.get()))
        button.grid(column=6, row=6, padx=5, pady=5)

        button = ttk.Button(frame, text="List clients", command=lambda: self._list_clients())
        button.grid(column=6, row=7, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Book id:")
        lbl.grid(column=0, row=8)

        rent_book_id = ttk.Entry(frame, {})
        rent_book_id.grid(column=1, row=8, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Client id:")
        lbl.grid(column=2, row=8)

        rent_client_id = ttk.Entry(frame, {})
        rent_client_id.grid(column=3, row=8, padx=5, pady=5)

        button = ttk.Button(frame, text="Rent a book",
                            command=lambda: self._rent_ui(rent_book_id.get(), rent_client_id.get()))
        button.grid(column=6, row=8, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Book id:")
        lbl.grid(column=0, row=9)

        return_book_id = ttk.Entry(frame, {})
        return_book_id.grid(column=1, row=9, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Client id:")
        lbl.grid(column=2, row=9)

        return_client_id = ttk.Entry(frame, {})
        return_client_id.grid(column=3, row=9, padx=5, pady=5)

        button = ttk.Button(frame, text="Return a book",
                            command=lambda: self._return_ui(return_book_id.get(), return_client_id.get()))
        button.grid(column=6, row=9, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Value:")
        lbl.grid(column=2, row=10)

        value_book = ttk.Entry(frame, {})
        value_book.grid(column=3, row=10, padx=5, pady=5)

        button = ttk.Button(frame, text="Search a book", command=lambda: self.search_book(value_book.get()))
        button.grid(column=6, row=10, padx=5, pady=5)

        lbl = ttk.Label(frame, text="Value:")
        lbl.grid(column=2, row=11)

        value_client = ttk.Entry(frame, {})
        value_client.grid(column=3, row=11, padx=5, pady=5)

        button = ttk.Button(frame, text="Search clients", command=lambda: self.search_client(value_client.get()))
        button.grid(column=6, row=11, padx=5, pady=5)

        button = ttk.Button(frame, text="Most rented books", command=lambda: self.most_rented_books())
        button.grid(column=6, row=12, padx=5, pady=5)

        button = ttk.Button(frame, text="Most active clients", command=lambda: self.most_active_clients())
        button.grid(column=6, row=13, padx=5, pady=5)

        button = ttk.Button(frame, text="Most rented author", command=lambda: self.most_rented_author())
        button.grid(column=6, row=14, padx=5, pady=5)

        button = ttk.Button(frame, text="Undo", command=lambda: self.undo())
        button.grid(column=6, row=15, padx=5, pady=5)

        button = ttk.Button(frame, text="Redo", command=lambda: self.redo())
        button.grid(column=6, row=16, padx=5, pady=5)

        button = ttk.Button(frame, text="Exit", command=lambda: frame.quit())
        button.grid(column=6, row=17, padx=5, pady=5)

        frame.mainloop()
