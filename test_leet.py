import unittest
from leet import leet

class TestLeet(unittest.TestCase):
    def test_get_leet_text(self):
        self.assertNotEqual(leet('hello'), 'hello')

    def test_only_integer(self):
        self.assertEqual('1234567890', '1234567890')

if __name__ == '__main__':
    unittest.main()
