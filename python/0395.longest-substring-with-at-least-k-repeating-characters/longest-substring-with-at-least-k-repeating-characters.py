class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if  s.count(c) < k:
                # split point
                return max([self.longestSubstring(t, k) for t in s.split(c)])
        # all elements' occurence are greater or equal to k, then return  lenght of s
        return len(s)