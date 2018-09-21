#!/usr/bin/env python2

import unittest
import answer_3


class TestAnswer3(unittest.TestCase):

    def test_create_dict_from_arguments(self):
        result = answer_3.create_dict_from_arguments(['a', 'b'], [1, 2])
        self.assertEquals(result, {'a': 1, 'b': 2})

    def test_create_dict_from_arguments_when_lists_not_equal_in_length(self):
        result = answer_3.create_dict_from_arguments(['a', 'b'], [1])
        self.assertEquals(result, {'a': 1, 'b': None})

    def test_create_dict_from_arguments_when_first_list_contains_numbers(self):
        result = answer_3.create_dict_from_arguments(['a', 1], [1, 2])
        self.assertEquals(result, {'a': 1, 1: 2})

    def test_create_dict_from_arguments_when_first_list_contains_a_boolean(self):
        result = answer_3.create_dict_from_arguments(['a', False], [1, 2])
        self.assertEquals(result, {'a': 1, False: 2})


if __name__ == '__main__':
    unittest.main()
