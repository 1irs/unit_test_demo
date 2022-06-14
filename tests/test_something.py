import unittest
import csv


def f1(a):

    try:
        res = 100/a
    except ZeroDivisionError:
        return 0
    return res


class SomethingTest(unittest.TestCase):

    def test_case_1(self):
        res = f1(0)
        self.assertEqual(0, res)
