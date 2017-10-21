import random

class Request:
    def __init__(self, p):
        self.requests = 0
        self.p = p
        self.discards = 0
        self.has_request = True

    def generate(self):
        if (random.random() > self.p):
            self.requests += 1
            self.has_request = True
        else:
            self.has_request = False

    def was_request(self):
        return self.has_request

    def get_requests(self):
        return self.requests

    def add_discard(self):
        self.discards += 1

    def get_discards(self):
        return self.discards
