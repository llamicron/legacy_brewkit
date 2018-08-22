import unittest

from ..str116 import STR116
from .. import relays


class TestRelays(unittest.TestCase):
    def setUp(self):
        self.str116 = STR116()

    def test_relay_class(self):
        relay = relays.Relay(4, self.str116)

        assert type(relay) is relays.Relay
        assert type(relay.controller) is STR116
        assert relay.address == 4

    def test_relay_get_and_set(self):
        relay = relays.Relay(3, self.str116)

        relay.set(1)
        assert relay.get() == 1
        relay.set(0)
        assert relay.get() == 0
