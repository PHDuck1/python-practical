import unittest


def quadratic_equation(a, b, c):
    d = b ** 2 - (4 * a * c)

    if d < 0:
        return None

    elif d == 0:
        try:
            return -b / (2 * a)
        except ZeroDivisionError:
            raise ValueError

    elif d > 0:
        try:
            return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
        except ZeroDivisionError:
            raise ValueError


class QuadraticEquationTest(unittest.TestCase):

    def test_d_less_zero(self):
        self.assertIsNone(quadratic_equation(4, 1, 2))

    def test_d_is_zero(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_d_more_zero(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)
