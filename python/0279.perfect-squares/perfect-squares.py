class Solution:
    def numSquares(self, n: int) -> int:
        # dp = [float('inf')] * (n + 1)
        # dp[0] = 0
        # for i in range(1, n+1):
        #     for j in range(1, int(i**0.5)+1):
        #         dp[i] = min(dp[i], dp[i-j*j]+1)
        # return dp[n]
        # 这里的办法非常巧妙，使用dp[-i*i] 逆向查，能够使得从较大的数分离，时间会快，前面注释的是从前向后，产生Time Limit Exceeded
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


