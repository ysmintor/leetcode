class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = skip = 0
        for num in nums:
            rob, skip = skip+num, max(rob, skip)
        return max(rob, skip)

#这个题目很有意思，开始想到的是通过数组记录 dp[i]代表当前最大收益，dp[i]=max(num[i]+dp[i-2], dpi[i-1])，后面看到文章说位置分 奇偶，又可以转化为 rob, skip 这种，实质还是 dp 的思想