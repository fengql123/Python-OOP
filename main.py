import csv


class Item:
    # class attribute
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validations
        assert price >= 0, f'Price: {price} is not at least 0!'
        assert quantity >= 0, f'Quantity: {quantity} is not at least 0!'
        # Instance Attribute
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)  # Append all instances to a list

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self, pay_rate):
        self.price = self.price * pay_rate

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
        return f'Item({self.name}, {self.price}, {self.quantity})'


Item.instantiate_from_csv()
print(Item.all)
