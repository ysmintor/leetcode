class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length//2):
            # caculate swap index
            j = length - 1 - i
            s[i],s[j] = s[j],s[i]
