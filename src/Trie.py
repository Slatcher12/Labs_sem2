class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_pattern = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_pattern = True

    def search(self, pattern):
        if self.root.children == {}:
            return False

        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_pattern

    def search_prefix(self, prefix):
        if self.root.children == {}:
            return False

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def get_tree_by_words(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie
