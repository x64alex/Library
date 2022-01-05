from src.services.UndoService import Call, Operation


class BookFunctionsService:
    def __init__(self, undo_service, repo_book, repo_rentals):
        self.func_rentals = repo_rentals
        self.func_books = repo_book
        self.books = self.func_books.books
        self.undo_service = undo_service

    def generate_books(self):
        self.func_books.generate_books()

    def add_book(self, book):
        """
        Add the new book to the list
        :param book: new book
        """

        book_id = book.id

        undo_call = Call(self._remove_book, book_id)
        redo_call = Call(self._add_book, book)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._add_book(book)

    def _add_book(self, book):
        self.func_books.add_book(book)

    def update_book(self, book_id, title, author):
        """
        Update the book with the given id with new title and new author
        :param book_id: given id
        :param title: new title
        :param author: new author
        """

        book = self.func_books.return_book_id(book_id)
        old_title = book.title
        old_author = book.author
        undo_call = Call(self._update_book, book_id, old_title, old_author)
        redo_call = Call(self._update_book, book_id, title, author)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._update_book(book_id, title, author)

    def _update_book(self, book_id, title, author):
        self.func_books.update_book(book_id, title, author)

    def remove_book(self, book_id):
        """
        Remove the book with the given id from the list
        :param book_id: given id
        """

        """
        Undo/Redo
        """
        book = self.func_books.return_book_id(book_id)

        undo_call = Call(self._add_book, book)
        redo_call = Call(self._remove_book, book_id)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._remove_book(book_id)

    def _remove_book(self, book_id):
        self.func_books.remove_book(book_id)

    def search_book(self, value):
        return self.func_books.search_book(value)

    def descending(self, book1, book2):
        return int(book1.id) < int(book2.id)

    def most_rented_books(self):
        rented_books = []
        books = self.func_books.books.get_list
        for book in books:
            rented_books.append([book, 0])
        rentals = self.func_rentals.rentals.get_list
        for rental in rentals:
            for rent in rented_books:
                if rent[0].id == rental.book_id:
                    rent[1] += 1

        def take_second(elem):
            return elem[1]

        rented_books.sort(key=take_second, reverse=True)

        return rented_books

    def most_rented_author(self):
        rented_authors = []
        books = self.func_books.books.get_list
        for book in books:
            ok = 1
            for rent in rented_authors:
                if rent[0] == book.author:
                    ok = 0

            if ok == 1:
                rented_authors.append([book.author, 0])

        for rental in self.func_rentals.rentals.get_list:
            for rent in rented_authors:
                book = self.func_books.return_book_id(rental.book_id)
                if book.author == rent[0]:
                    rent[1] += 1

        def take_second(elem):
            return elem[1]

        rented_authors.sort(key=take_second, reverse=True)

        return rented_authors
