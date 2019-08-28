class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = {}
        for i in range(0, len(words)):
            self.d[words[i]] = self.d.get(words[i], []) + [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.d[word1]
        l2 = self.d[word2]
        i = j = 0
        ans = float("inf")
        while i < len(l1) and j < len(l2):
            ans = min(ans, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return ans

# Your WordDistance object will be instantiated and called as such:

words = ["practice", "makes", "perfect", "coding", "makes"]
wordDistance = WordDistance(words)
dws1 = wordDistance.shortest("practice", "coding")
print("dws1=", dws1)
dws2=wordDistance.shortest("practice", "makes")
print("dws2=", dws2)