from .str116 import STR116

class Relay(object):
    def __init__(self, address, controller):
        self.address = address
        assert type(controller) is STR116
        self.controller = controller

    def get(self):
        return self.controller.get_relay(self.address)

    def set(self, state):
        self.controller.set_relay(self.address, state)



def Binary(address, controller):
    rel = Relay(address, controller)
    rel.possible_states = {
        0: 'closed',
        1: 'open'
    }
    return rel

def Divert(address, controller, possible_states):
    rel = Relay(address, controller)
    rel.possible_states = possible_states
    return rel

def Pump(address, controller):
    rel = Relay(address, controller)
    rel.possible_states = {
        0: 'off',
        1: 'on'
    }
    return rel
