class Solution:
    # 依据规律出来，发现就是卡特兰数，故第二种直接求卡特兰数
    def _numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0]=dp[1]=1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]

    def numTrees(self, n: int) -> int:
        ans = 1
        for i in range(1, n+1):
            ans = ans*(n+i)//i
        return ans//(n+1)