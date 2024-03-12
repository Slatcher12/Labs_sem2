import unittest
from lab1.src.lab1_2sem import longest_peak


class TestFindLongestPick(unittest.TestCase):
    def test_give_list(self):
        result = longest_peak([1, 2, 4, 3, 2, 5, 1, 10])
        self.assertEqual(result, 5)

    def test_sort_list(self):
        result = longest_peak([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result, 0)

    def test_pick_with_double_same_value(self):
        result = longest_peak([1, 2, 3, 5, 5, 2])
        self.assertEqual(result, 0)

    def test_single_element_list(self):
        result = longest_peak([5])
        self.assertEqual(result, 0)


if __name__ == "__main":
    unittest.main()