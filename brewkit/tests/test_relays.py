import unittest

from ..str116 import STR116
from .. import relays


class TestRelays(unittest.TestCase):
    def setUp(self):
        self.str116 = STR116()

    def test_binary_class(self):
        bin = relays.Binary(4, self.str116)

        assert type(bin) is relays.Binary
        assert type(bin.controller) is STR116
        assert bin.address == 4

    def test_binary_get_and_set(self):
        bin = relays.Binary(3, self.str116)

        bin.set(1)
        assert bin.get() == 1
        bin.set(0)
        assert bin.get() == 0
