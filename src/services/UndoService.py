class UndoService:
    """
    How can we implement multiple undo/redo with cascade?

    Keep track of program operations and reverse them (undo) / repeat them (redo)
        => Command design pattern
        (command = tell the program to do something, but later)
    """

    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        self._history.append(operation)
        self._index = len(self._history) - 1

    def undo(self):
        print(len(self._history))

        if self._index == -1 or self._index >= len(self._history):
            return
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        print(len(self._history), self._index)

        if self._index == -1:
            self._index = 0
        if self._index >= len(self._history):
            return
        self._history[self._index].redo()
        self._index += 1


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)


'''
    private ArrayList<Operation> history;
'''


class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()
