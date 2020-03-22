import unittest

import ddt

import simple


@ddt.ddt
class TestSimple(unittest.TestCase):

    def test_one_case(self):
        result = simple.check_simple(10)
        self.assertFalse(result)

    @ddt.data(0, 14, 16, 15)
    def test_false_cases(self, num):
        """Test {} is not a simple number"""
        result = simple.check_simple(num)
        self.assertFalse(result)

    @ddt.data(
        (2, True),
        (3, True),
        (5, True),
        (0, False),
        (4, False),
        (12, False),
        (15, False),
        (33, False),
    )
    @ddt.unpack
    def test_different_cases(self, num, expected):
        """Test {} is  a simple number {}"""
        result = simple.check_simple(num)
        self.assertEqual(result, expected)

    # nosetests -s tests/test_simple.py:TestSimple.test_bad_nums
    # nosetests -s tests --with-coverage --cover-erase
    # nosetests -s tests --with-coverage --cover-erase --cover-package=./src

    def test_bad_nums(self):
        # result = simple.check_simple(-5)
        # self.assertFalse(result)
        with self.assertRaises(TypeError):
            simple.check_simple(-5)
