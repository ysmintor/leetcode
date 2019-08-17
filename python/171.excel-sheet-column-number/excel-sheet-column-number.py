class Solution(object):
    # 这个题目实际上就是一个二十六进制转换为十进制的算法
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,"M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,"X": 24, "Y": 25, "Z": 26}
        s = s.upper()
        ret = 0
        b = 0
        for c in reversed(s):
            ret += letters[c] * 26 ** (b)
            b += 1
        return ret

    # another little trick to solve this problem
    # use ord() to get ascii number
    def titleToNumber2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ensure all alphabet are upper case
        s = s.upper()
        ret = 0
        b = 0
        for c in reversed(s):
            ret += (ord(c) - ord('A') + 1) * 26 ** (b)
            b += 1
        return ret