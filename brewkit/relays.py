from .str116 import STR116

class Binary(object):
    def __init__(self, address, controller):
        self.address = address
        assert type(controller) is STR116
        self.controller = controller

        # This is temporary
        self.state = 1

    def get(self):
        return self.state

    def set(self, state):
        self.state = state
