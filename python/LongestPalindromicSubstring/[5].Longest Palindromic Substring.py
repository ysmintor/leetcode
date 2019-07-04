# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
"""
Time complexity O(n^2)
Space complexity O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            lenx = max(len1, len2)
            if lenx > end - start:
                start = i - (lenx - 1) // 2
                end = i + lenx // 2
        return s[start: end + 1]


    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        L, R = left, right
        while(L >= 0 and R < len(s) and s[L] == s[R]):
            L-=1
            R+=1
        return R-L-1
