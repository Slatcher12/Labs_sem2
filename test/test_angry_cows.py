import unittest
from src.angry_cows import get_max_width


class TestFindLongestPick(unittest.TestCase):
    def test_given_list_of_cows(self):
        result = get_max_width(cows=3, free_sections=[1, 2, 8, 4, 9])
        self.assertEqual(result, 3)

    def test_sorted_list_of_cows(self):
        result = get_max_width(cows=4, free_sections=[1, 2, 8, 14, 29, 22])
        self.assertEqual(result, 7)

    def test_big_value_list_of_cows(self):
        result = get_max_width(cows=4, free_sections=[1, 2, 3, 99, 5, 47, 30, 40, 65, 93, 123])
        self.assertEqual(result, 30)


if __name__ == "__main":
    unittest.main()