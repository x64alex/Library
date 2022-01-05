import copy
import unittest


class DataStructure:
    def __init__(self, given_list) -> None:
        self.list = given_list

    def __setitem__(self, key, value):
        self.list[key] = value

    def __getitem__(self, item):
        return self.list[item]

    def __delitem__(self, key):
        self.list.remove(self.list[key])

    def __next__(self):
        if self.i < len(self.list):
            res = self.list[self.i]
            self.i += 1
            return res

    def __iter__(self):
        self.i = 0
        return self

    def __len__(self):
        return len(self.list)

    def append(self, el):
        self.list.append(el)

    def pop(self, index=-1):
        if index == -1:
            self.list.pop()
        else:
            self.list.pop(index)

    def index(self, bk):
        return self.list.index(bk)

    @property
    def get_list(self):
        return self.list

    def shell_sort(self, comparison, array=''):
        """
        Shell sort
        :param comparison:
        :param array:
        :return:
        """
        if array == '':
            array = self.list
        n = len(array)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and comparison(array[j - interval], temp):
                    array[j] = array[j - interval]
                    j -= interval

                array[j] = temp
            interval //= 2

    def filter_function(self, acceptance_function, given_list=''):
        new_list = []
        if given_list == '':
            given_list = self.list
        for el in given_list:
            if acceptance_function(el):
                new_list.append(el)

        return new_list


class Tests(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_data_structure(self):
        data_structure = DataStructure([1, 8, 4, 5, 6, 7])
        assert data_structure.list == [1, 8, 4, 5, 6, 7]
        assert len(data_structure) == 6
        data_structure[1] = 5
        assert data_structure[1] == 5
        data_structure[1] = 8

        def descending(x, y):
            return x < y

        def ascending(x, y):
            return x > y

        data_structure.shell_sort(descending)
        assert data_structure.get_list == [8, 7, 6, 5, 4, 1]

        data_structure.shell_sort(ascending)
        assert data_structure.get_list == [1, 4, 5, 6, 7, 8]

        def even(x):
            return x % 2 == 0

        assert data_structure.filter_function(even) == [4, 6, 8]
        data_structure.pop(0)
        data_structure.pop(2)
        data_structure.__delitem__(1)
        assert data_structure.get_list == [4, 7, 8]
        iter(data_structure)
        assert next(data_structure) == 4
        assert next(data_structure) == 7
        data_structure.append(2)
        assert data_structure.get_list == [4, 7, 8, 2]
        data_structure.pop()
        assert data_structure.get_list == [4, 7, 8]
        assert data_structure.index(8) == 2
        data_structure.append(2)
        data_structure.append(3)
        data_structure.pop(1)
        assert data_structure.get_list == [4, 8, 2, 3]
