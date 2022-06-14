import unittest

from find_square_roots import find_square_roots


class FindSquareRootsTest(unittest.TestCase):

    def test_one_root(self):
        # Act (действие)
        result = find_square_roots(1, 12, 36)

        # Assert (проверка)
        # Ожидание: (-6.0, None)
        self.assertEqual(
            (-6.0, None),  # Ожидание (expect, expectation)
            result         # Актуальный результат (actual, result)
        )

    def test_two_roots(self):
        result = find_square_roots(1, -2, -3)
        self.assertEqual(
            (-1, 3),  # Ожидание (expect, expectation)
            result         # Актуальный результат (actual, result)
        )

    def test_no_roots(self):
        result = find_square_roots(1, 0, 10)
        self.assertEqual(
            (None, None),  # Ожидание (expect, expectation)
            result         # Актуальный результат (actual, result)
        )
