from src.repository.repository import RentalFunctions, RentalFunctionsBin, RentalFunctionsTextFile, ClientFunctions, \
    ClientFunctionsBin, ClientFunctionsTextFile, BookFunctions, BookFunctionsBin, BookFunctionsTextFile
from src.ui.ui import UI
from src.ui.gui import GUI
from src.services.book_service import BookFunctionsService
from src.services.client_service import ClientFunctionsServices
from src.services.rental_service import RentalFunctionsServices
from src.services.UndoService import UndoService


def service(undo_service, repo_book, repo_client, repo_rental,
            ui_class):
    book_service = BookFunctionsService(undo_service, repo_book, repo_rental)
    client_service = ClientFunctionsServices(undo_service, repo_client, repo_rental)
    rental_service = RentalFunctionsServices(undo_service, repo_rental)

    return ui_class(undo_service, book_service, client_service, rental_service)


def load_file(file):
    f = open(file, "rt")  # rt -> read, text-mode
    data = []
    for line in f.readlines():
        text, repo = line.split(maxsplit=1, sep='=')
        repo = repo[1:len(repo) - 1]
        data.append(repo)

    f.close()
    return data[0], data[1], data[2], data[3], data[4]


def start():
    repo, book_file, client_file, rental_file, ui = load_file("settings.properties.txt")
    undo_service = UndoService()
    repo_rental = RentalFunctions()
    repo_client = ClientFunctions()
    repo_book = BookFunctions()
    if repo == 'binary':
        repo_rental = RentalFunctionsBin(rental_file)
        repo_client = ClientFunctionsBin(client_file)
        repo_book = BookFunctionsBin(book_file)
    elif repo == 'text':
        repo_rental = RentalFunctionsTextFile(rental_file)
        repo_client = ClientFunctionsTextFile(client_file)
        repo_book = BookFunctionsTextFile(book_file)
    elif repo != 'inmemory':
        return

    if ui == 'UI':
        app = service(undo_service, repo_book, repo_client, repo_rental, UI)
        app.start()
    elif ui == 'GUI':
        app = service(undo_service, repo_book, repo_client, repo_rental, GUI)
        app.start()


start()
"""
repository = inmemory
book = ''
clients = ''
rentals = ''
ui = GUI

repository = text
book = book.txt
clients = client.txt
rentals = rental.txt
ui = GUI

repository = binary
book = book.bin
clients = client.bin
rentals = rental.bin
ui = UI

"""