class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.trie
        for s in word:
            if s not in tree:
                # insert a new tree
                tree[s] = {}
            tree = tree[s]
        # end tag
        tree['#']='#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.trie
        for s in word:
            if s not in tree:
                return False
            # enter next tree
            tree = tree[s]
        # check end tag
        return True if '#' in tree else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.trie
        for s in prefix:
            if s not in tree:
                return False
            tree = tree[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)