class Solution:
    # DP solution
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_length = len(s)
        dp = [None]*(word_length+1)
        word_set = set(wordDict)
        dp[0] = True
        for i in range(word_length+1):
            for  j in range(i):
                if dp[j] and (s[j:i] in word_set):
                    dp[i] = True
                    break
        return dp[word_length]