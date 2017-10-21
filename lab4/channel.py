import random

class Channel:
    def __init__(self, p):
        self.outs = 0
        self.discards = 0
        self.processed = True
        self.value = 0
        self.p = p

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def get_processed(self):
        return self.processed

    def change_processed(self):
        self.processed = not self.processed

    def set_processed(self, processed):
        self.processed = processed

    def generate(self):
        self.processed = True if random.random() > self.p else False

    def add_out(self):
        self.outs += 1

    def add_discard(self):
        self.discards += 1

    def get_outs(self):
        return self.outs

    def get_discards(self):
        return self.discards
