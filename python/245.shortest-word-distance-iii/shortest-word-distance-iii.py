class Solution:
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
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = float("inf")
        idx1 = idx2 = -1
        for i in range(0, len(words)):
            word = words[i]
            if word in (word1, word2):
                if word == word1:
                    idx1 = i
                    if idx2 != -1 and idx1 != idx2:
                        ans = min(ans, abs(idx2 - idx1))
                if word == word2:
                    idx2 = i
                    if idx1 != -1 and idx1 != idx2:
                        ans = min(ans, abs(idx2 - idx1))
        return ans

words = ["practice", "makes", "perfect", "coding", "makes"]
wordDistance = Solution(words)
dws1 = wordDistance.shortest("practice", "coding")
print("dws1=", dws1)
dws2=wordDistance.shortest("practice", "makes")
print("dws2=", dws2)