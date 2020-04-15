import ddt
import task4 as test_module4
import unittest


@ddt.ddt
class EulerMaximumTest(unittest.TestCase):
    """Testing on Euler maximum function"""

    @ddt.data(-1, 's', 0)
    def test_raises(self, data):
        """{} not raised Type error"""
        with self.assertRaises(TypeError):
            test_module4.maximum_of_euler_function(data)

    @ddt.data(
        (1, (1, 1)),
        (6, (6, 2)),
        (10, (6, 2)),
        (29, (6, 2)),
        (30, (30, 8)),
        (209, (30, 8)),
        (210, (210, 48)),
        (1000000, (510510, 92160)),
    )
    @ddt.unpack
    def test_result(self, data, expected):
        """test f({}) not equal to {}"""
        self.assertEqual(
            test_module4.maximum_of_euler_function(data), expected
        )
