import random

class Channel:
    def __init__(self, m,v,y):
        self.m = m
        self.v = v
        self.y = y

        self.valid_value = 0
        self.broken_value = 0

        self.was_processed = True
        self.was_repared = True
        self.was_broken = False

        self.outs = 0
        self.discards = 0

    def generate(self):
        self.was_processed = True if random.random() > self.m else False
        self.was_repared = True if random.random() > self.y and not self.was_broken else False
        self.was_broken = True if random.random() > self.v and not self.was_repared else False

    def add_out(self):
        self.outs += 1

    def add_discard(self):
        self.discards += 1

    def get_outs(self):
        return self.outs

    def get_discards(self):
        return self.discards
