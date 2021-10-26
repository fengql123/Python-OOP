from item import Item


class Phone(Item):  # Child Class
    def __init__(self, name: str, price: float, quantity: int = 0, condition='new'):
        # super class is responsible for inheritance of all instances and methods
        super().__init__(name, price, quantity)
        self.condition = condition

    def __repr__(self):
        return super().__repr__()
