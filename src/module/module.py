import copy
import unittest


class DataStructure:
    def __init__(self, given_list):
        self.list = given_list

    def shell_sort(self, comparison, array=''):
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
        if given_list == '':
            given_list = self.list
        for el in given_list:
            if not acceptance_function(el):
                given_list.pop(given_list.index(el))



class Tests(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_data_structure(self):
        data_structure = DataStructure([1, 8, 4, 5, 6, 7])
        assert data_structure.list == [1, 8, 4, 5, 6, 7]

        def descending(x, y):
            return x < y

        def ascending(x, y):
            return x > y

        data_structure.shell_sort(descending)
        assert data_structure.list == [8, 7, 6, 5, 4, 1]

        data_structure.shell_sort(ascending)
        assert data_structure.list == [1, 4, 5, 6, 7, 8]

        def even(x):
            return x % 2 == 0

        data_structure.filter_function(even)
        assert data_structure.list == [4, 6, 8]
