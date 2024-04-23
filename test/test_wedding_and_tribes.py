import unittest
from src.wedding_and_tribes import check_amount_of_pairs


class TestCheckAmountOfPairs(unittest.TestCase):
    def test_check_amount_of_pairs(self):
        check_amount_of_pairs("wedding_input.txt", "wedding_output.txt")
        with open(
                f"D:/Workspace/Labs_sem2/resources/wedding_output.txt",
                "r",
                encoding="utf-8",
        ) as file:
            result = file.readline().strip()
        self.assertEqual(result, "amount of pairs is 3")


if __name__ == "__main__":
    unittest.main()