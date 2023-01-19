import unittest


class TriangleNotValidArgumentException(Exception):

    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):

    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:

    def __init__(self, sides):
        self.sides = sides

        if not isinstance(sides, tuple) or not all(isinstance(side, int) or isinstance(side, float) for side in sides) or len(sides) != 3:
            raise TriangleNotValidArgumentException

        try:
            if (sides[0] + sides[1] <= sides[2] or
                    sides[1] + sides[2] <= sides[0] or
                    sides[0] + sides[2] <= sides[1]):
                raise TriangleNotExistException

        except (ValueError, TypeError):
            raise TriangleNotValidArgumentException

    def get_area(self):
        p = sum(self.sides) / 2
        a, b, c = self.sides
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class TriangleTest(unittest.TestCase):

    def test_valid_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            Triangle((1, 2, 3))

        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle((7, "str", 7))

    def test_get_area(self):
        self.assertEqual(Triangle((3, 4, 5)).get_area(), 6.0)

    def test_valid_arguments(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle((7, "str", 7))
