from src.services.UndoService import Call, Operation


class RentalFunctionsServices:
    def __init__(self, undo_service, repo_rental):
        self.func_rental = repo_rental
        self.rentals = self.func_rental.rentals
        self.undo_service = undo_service

    def rent(self, book, client_id):
        undo_call = Call(self.func_rental.rent_delete, book, client_id)
        redo_call = Call(self._rent, book, client_id)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._rent(book, client_id)

    def returned(self, book, client_id):
        undo_call = Call(self.func_rental.returned_delete, book, client_id)
        redo_call = Call(self._returned, book, client_id)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._returned(book, client_id)

    def _rent(self, book, client_id):
        self.func_rental.rent(book, client_id)

    def _returned(self, book, client_id):
        self.func_rental.returned(book, client_id)
