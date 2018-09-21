#!/usr/bin/env python2

import unittest
import answer_2


class TestAnswer2(unittest.TestCase):

    def test_create_list_from_argument_when_a_number(self):
        result = answer_2.create_list_from_argument(1)
        self.assertEquals(result, ['1'])

    def test_create_list_from_argument_when_a_dict(self):
        result = answer_2.create_list_from_argument({'hello': 1, 'goodbye': 2})
        self.assertEquals(result, ['hello', 'goodbye'])

    def test_create_list_from_argument_when_a_string(self):
        result = answer_2.create_list_from_argument('hello')
        self.assertEquals(result, ['h', 'e', 'l', 'l', 'o'])

    def test_create_list_from_argument_when_a_none(self):
        result = answer_2.create_list_from_argument(None)
        self.assertEquals(result, [])

    def test_create_list_from_argument_when_a_list(self):
        result = answer_2.create_list_from_argument(['hello', 'goodbye'])
        self.assertEquals(result, ['hello', 'goodbye'])


if __name__ == '__main__':
    unittest.main()
