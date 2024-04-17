import unittest
from src.undirected_graph_cycle import check_for_cycle_in_graph


class TestCycleDetection(unittest.TestCase):
    def test_is_cycle_function_runs(self):
        check_for_cycle_in_graph("graph_input.txt", "graph_output.txt")
        with open(
                f"../resources/graph_output.txt",
                "r",
                encoding="utf-8",
        ) as file:
            result = file.readline()
        self.assertTrue(result, "graph has cycle")


if __name__ == "__main__":
    unittest.main()
