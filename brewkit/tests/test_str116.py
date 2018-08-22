import unittest

from ..str116 import STR116

class TestSTR116(unittest.TestCase):
    def test_class_defaults(self):
        s = STR116()
        assert type(s) is STR116
        assert s.port == '/dev/ttyAMA0'
        assert s.address == 2
