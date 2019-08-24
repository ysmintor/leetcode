class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0]*26
        for i in range(0, len(s)):
            table[ord(s[i])-ord('a')] += 1
        for i in range(0, len(t)):
            pos = ord(t[i])-ord('a')
            table[pos] -= 1
            if table[pos] < 0:
                return False
        return True
