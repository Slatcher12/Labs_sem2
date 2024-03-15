import unittest
from src.gorila_jacky import get_max_eating_speed


class TestFindLongestPick(unittest.TestCase):
    def test_given_list_of_gorilla(self):
        result = get_max_eating_speed(piles=[3,6,7,11], hours_before_security=8)
        self.assertEqual(result, 4)

    def test_sorted_list_of_gorilla(self):
        result = get_max_eating_speed(piles=[30,11,23,4,20], hours_before_security=5)
        self.assertEqual(result, 30)

    def test_big_value_list_of_gorilla(self):
        result = get_max_eating_speed(piles=[30,11,23,4,20], hours_before_security=6)
        self.assertEqual(result, 23)


if __name__ == "__main":
    unittest.main()
