class Solution:
    # 两种都是 DP 解决，一个是 O(n)空间，下面一个是O(1)空间，关键在于怎么去理解 dp[i]的含义，第一种代表是当前步骤能向后跳一到两个
    # 所以需要判断最后两个中的最小的一个
    # 第二个方法则则表示到当前台阶时，前面所需要的步骤，假定一个 len(cost)+1，到这个一定是结束，所以最后直接返回，不用再进行大小判断
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]
        dp[3] = 4
        for i in range(2, length):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[i-1], dp[i])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a, b = b, c
        return b