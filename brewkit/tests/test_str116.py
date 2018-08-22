import unittest

from ..str116 import STR116

class TestSTR116(unittest.TestCase):
    def test_class_defaults(self):
        s = STR116()
        assert type(s) is STR116
        assert s.port == '/dev/ttyAMA0'
        assert s.address == 2

    def test_get_relay(self):
        s = STR116()

        assert s.get_relay(3) in (0, 1)

    def test_set_relay(self):
        s = STR116()

        s.set_relay(3, 1)
        assert s.get_relay(3) == 1
        s.set_relay(3, 0)
        assert s.get_relay(3) == 0

