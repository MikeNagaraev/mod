class Queue:
    def __init__(self, n):
        self.max_items = n
        self.items = 0

        self.discards = 0


    def add_item(self):
        if (self.items < self.max_items):
            self.items += 1
            self.discards += 1

    def remove_item(self):
        if (self.items > 0):
            self.items -= 1

    def is_full(self):
        return self.items == self.max_items

    def is_empty(self):
        return self.items == 0

    def get_value(self):
        return self.items

    def get_discards(self):
        return self.discards
