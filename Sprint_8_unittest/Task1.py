import unittest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total_price(self):
        if self.count > 20:
            discount = 0.5

        elif self.count == 20:
            discount = 0.7

        elif self.count >= 10:
            discount = 0.8

        elif self.count >= 7:
            discount = 0.9

        elif self.count >= 5:
            discount = 0.95

        else:
            discount = 1

        return self.count * self.price * discount


class Cart:

    def __init__(self, products):
        self.products = products

    def get_total_price(self):
        return sum(prod.total_price() for prod in self.products)


class CartTest(unittest.TestCase):

    def setUp(self):
        self.products = (Product('p1',10,4),
                    Product('p2',100,5),
                    Product('p3',200,6),
                    Product('p4',300,7),
                    Product('p5',400,9),
                    Product('p6',500,10),
                    Product('p7',1000,20))

    def test_get_total_price(self):
        cart = Cart(self.products)
        self.assertEqual(cart.get_total_price(), 24785.0)
