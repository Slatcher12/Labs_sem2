def compare_tree(self_root, other_root):
    if self_root is None and other_root is None:
        return True

    if self_root is not None and other_root is not None:
        return self_root.value == other_root.value and \
            compare_tree(self_root.left, other_root.left) and \
            compare_tree(self_root.right, other_root.right)

    return False


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def equal(self, other):
        if other is None:
            return False

        return compare_tree(self, other)


def invert_tree(tree: BinaryTree):
    if tree is None:
        return tree

    invert_tree(tree.left)
    invert_tree(tree.right)
    tree.left, tree.right = tree.right, tree.left

    return tree



