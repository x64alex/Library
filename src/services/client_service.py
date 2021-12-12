from src.services.UndoService import Call, CascadedOperation, Operation
from datetime import date


class ClientFunctionsServices:
    def __init__(self, undo_service, repo_client, repo_rentals):
        self.func_rentals = repo_rentals
        self.func_clients = repo_client
        self.clients = self.func_clients.clients
        self.undo_service = undo_service

    def generate_clients(self):
        self.func_clients.generate_clients()

    def add_clients(self, client):
        client_id = client.id

        undo_call = Call(self._remove_client, client_id)
        redo_call = Call(self._add_clients, client)
        cope = CascadedOperation()

        cope.add(Operation(undo_call, redo_call))

        self.undo_service.record(Operation(undo_call, redo_call))
        self._add_clients(client)

    def _add_clients(self, client):
        self.func_clients.add_client(client)

    def update_client(self, client_id, name):
        """
        Update the client with the given id with new name
        :param client_id: given id
        :param name: given name
        """

        client = self.func_clients.return_client_id(client_id)
        old_name = client.name
        undo_call = Call(self._update_client, client_id, old_name)
        redo_call = Call(self._update_client, client_id, name)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._update_client(client_id, name)

    def _update_client(self, client_id, name):
        self.func_clients.update_client(client_id, name)

    def remove_client(self, client_id):
        """
        Remove the client with the given id
        :param client_id: given id
        """
        client = self.func_clients.return_client_id(client_id)

        undo_call = Call(self._add_clients, client)
        redo_call = Call(self._remove_client, client_id)

        self.undo_service.record(Operation(undo_call, redo_call))

        self._remove_client(client_id)

    def _remove_client(self, client_id):
        self.func_clients.remove_client(client_id)

    def search_clients(self, value):
        return self.func_clients.search_clients(value)

    def most_active_clients(self):
        active_clients = []
        clients = self.func_clients.clients
        for client in clients:
            active_clients.append([client, 0])

        for rental in self.func_rentals.rentals:
            for client in active_clients:
                if client[0].id == rental.client_id:
                    d = date(int(rental.rented[0:4]), int(rental.rented[5:7]), int(rental.rented[8:10]))
                    day = date.today()
                    if rental.returned != 'not returned':
                        day = date(int(rental.returned[0:4]), int(rental.returned[5:7]), int(rental.returned[8:10]))
                    delta = day - d
                    client[1] = client[1] + delta.days + 1
                    print(client[1])

        def take_second(elem):
            return elem[1]

        active_clients.sort(key=take_second, reverse=True)

        return active_clients
