import unittest
from src.Trie import Trie, get_tree_by_words


class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("pineapple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)

    def test_search_prefix(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("applepen")
        trie.insert("pineapplepen")
        self.assertEqual(trie.search_prefix("app"), True)
        self.assertEqual(trie.search_prefix("pinn"), False)

    def test_empty_search(self):
        trie = Trie()
        self.assertEqual(trie.search("apple"), False)
        self.assertEqual(trie.search_prefix("app"), False)

    def test_get_tree_by_words(self):
        trie = get_tree_by_words(["apple", "blitz", "applepen", "pinapplepen"])
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.search_prefix("app"), True)
        self.assertEqual(trie.search_prefix("pinn"), False)


if __name__ == "__main":
    unittest.main()
