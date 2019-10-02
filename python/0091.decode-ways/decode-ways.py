class Solution:
    # 没有想到这个题目是动态规划的题目，而且和 climb stair 有相近的解题思路
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == '0':
            return 0

        dp = [1, 1]
        for i in range(2,len(s) + 1):
            if 10 <= int(s[i - 2 : i]) <=26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i-2 : i]) == 10 or int(s[i - 2 : i]) == 20:
                dp.append(dp[i - 2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0

        return dp[len(s)]
    # 使用 O(1)空间求解
    def numDecodings2(self, s: str) -> int:
        a,b = 1, 1
        for i in range(1, len(s)):
            if int(s[i]) == 0:
                b = 0
            if int(s[i-1]) == 1 or int(s[i-1]) == 2 and int(s[i]) <= 6:
                b = a + b
                a = b - a
            else:
                a = b
        return b