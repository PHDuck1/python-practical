from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class FetuchineAlphredo(Product):
    name = "Fetuchine Alphredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")


