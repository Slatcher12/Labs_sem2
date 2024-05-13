import unittest
from src.flower_shop import flowers_max_flow


class TestFlowersMaxFlow(unittest.TestCase):
    def test_farms_stores_graph(self):
        result = flowers_max_flow("roads.csv")
        self.assertEqual(result, 10)

    def test_empty_input(self):
        result = flowers_max_flow("empty_input.txt")
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()

