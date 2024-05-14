import unittest
from src.word_chain import word_chain


class TestWordChain(unittest.TestCase):
    def test_word_chain(self):
        result = word_chain("wchain_input.txt")
        self.assertEqual(result, 6)

    def test_empty_input(self):
        result = word_chain("empty_input.txt")
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()

