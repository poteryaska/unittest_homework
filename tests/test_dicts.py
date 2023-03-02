import unittest
from utils import dicts

class TestDicts(unittest.TestCase):
    def test_get_val(self):
        self.assertEqual(dicts.get_val({1: 2, 2: 4, 3: 9}, 3), 9)
        self.assertEqual(dicts.get_val({}, 3), 'git')