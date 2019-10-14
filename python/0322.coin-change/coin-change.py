class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_amount = amount + 1
        dp = [max_amount] * (max_amount)
        dp[0] = 0
        for rem in range(amount+1):
            for coin in coins:
                if coin <= rem:
                    dp[rem] = min(dp[rem], dp[rem-coin]+1)
        return -1 if dp[-1] > amount else dp[-1]

"""
典型的背包问题，相比于0-1背包要复杂一些，两层循环来讲，时间复杂度比较高了。
只不过自己对于自顶向下，即递归的方式还不太理解，以后有时间针对背包问题总结一下。
"""