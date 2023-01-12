class Goods:

    def __init__(self, price, discount_strategy=lambda x: x):
        self.price = price
        self.discount_strategy = discount_strategy

    @property
    def price_after_discount(self):
        return self.discount_strategy(self.price)

    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount}"


def on_sale_discount(order):
    return order * 0.5


def twenty_percent_discount(order):
    return order * 0.8
