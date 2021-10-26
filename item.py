import csv


class Item:
    # class attribute
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validations
        assert price >= 0, f'Price: {price} is not at least 0!'
        assert quantity >= 0, f'__Quantity: {quantity} is not at least 0!'
        # Instance Attribute
        self.__name = name  # makeing the instance private
        self.__price = price
        self.__quantity = quantity
        # Actions to execute
        Item.all.append(self)  # Append all instances to a list

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @name.setter
    def name(self, v):
        self.__name = v

    @quantity.setter
    def quantity(self, q):
        self.__quantity = q

    def calculate_total_price(self):
        return self.__quantity * self.__price

    def apply_discount(self, pay_rate):
        self.__price = self.__price * pay_rate  # Encapsulation in action

    def __connect(self):  # private methods
        pass

    def send(self):  # Simulation of Abstraction
        self.__connect()
        pass

    # Class Method (Straight away use on the class)

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                item['name'],
                float(item[' price']),
                float(item[' quantity'])
            )

    # Static Method (like a function not related with the instances)
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Representing Objects
    def __repr__(self):
        # Auto fill the name
        return f'{self.__class__.__name__}({self.__name}, {self.__price}, {self.__quantity})'
