# Construct a Product class using Builder.
# Focus points
#  - method chaining
#  - format price when printing
from patterns.creational import singleton

class Product:

    def __init__(self, weight, price, ship_volume, ship_code, title):
        self.weight = weight
        self.price = price
        self.ship_volume = ship_volume
        self.ship_code = ship_code
        self.title = title


class ProductBuilder:


    def __init__(self):
        self.product = None
        self.weight = 0
        self.price = 0.0
        self.ship_volume = 0
        self.ship_code = 0
        self.title = ""

    def with_weight(self, weight):
        self.weight = weight
        return self

    def with_price(self, price):
        self.price = price
        return self

    def with_ship_volume(self, ship_volume):
        self.ship_volume = ship_volume
        return self


    def with_ship_code(self, ship_code):
        self.ship_code = ship_code
        return self

    def with_title(self, title):
        self.title = title
        return self

    def build(self):
        product2 = singleton.Product.get_instance()
        product2.weight = 100
        self.product = Product(self.weight, self.ship_volume, self.ship_volume, self.ship_code, self.title)
        return self.product
