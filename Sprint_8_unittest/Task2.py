import unittest


def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):

    def test_divide_simple(self):
        self.assertAlmostEqual(divide(1, 3), 0.333333, 5)

    def test_divide_negative(self):
        self.assertAlmostEqual(divide(-5, -10), 0.5, 4)
        self.assertAlmostEqual(divide(-5, 10), -0.5, 4)
        self.assertAlmostEqual(divide(5, -10), -0.5, 4)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(0.8, -0.3), -2.666666, 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
