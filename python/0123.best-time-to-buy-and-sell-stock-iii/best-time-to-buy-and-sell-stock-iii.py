class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i10, dp_i11 = 0, float('-inf')
        dp_i20, dp_i21 = 0, float('-inf')
        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)

        return dp_i20
