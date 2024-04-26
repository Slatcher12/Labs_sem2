class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        if self.root.children == {}:
            return False

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

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
