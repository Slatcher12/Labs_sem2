import unittest
from src.inversion_of_tree import invert_tree, BinaryTree


class TestFindLongestPick(unittest.TestCase):
    def test_given_list_of_trees(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        predicted_root = BinaryTree(1)
        predicted_root.left = BinaryTree(3)
        predicted_root.right = BinaryTree(2)

        predicted_root.right.left = BinaryTree(5)
        predicted_root.right.right = BinaryTree(4)
        predicted_root.left.left = BinaryTree(7)
        predicted_root.left.right = BinaryTree(6)

        result = invert_tree(root)
        self.assertTrue(result.equal(predicted_root))


if __name__ == "__main":
    unittest.main()
