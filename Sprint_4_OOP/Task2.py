import itertools


class Pizza:
    made = {
        'hawaiian': ['ham', 'pineapple'],
        'meat_festival': ['beef', 'meatball', 'bacon'],
        'garden_feast': ['spinach', 'olives', 'mushroom']
    }

    newid = itertools.count()
    next(newid)

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = next(Pizza.newid)

    @classmethod
    def hawaiian(cls):
        return Pizza(cls.made['hawaiian'])

    @classmethod
    def meat_festival(cls):
        return Pizza(cls.made['meat_festival'])

    @classmethod
    def garden_feast(cls):
        return Pizza(cls.made['garden_feast'])
