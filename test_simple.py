import unittest


class SimpleTest(unittest.TestCase):

    def test(self):
        """2 + 2 = 4"""
        self.assertEqual(4, 2 + 2)
