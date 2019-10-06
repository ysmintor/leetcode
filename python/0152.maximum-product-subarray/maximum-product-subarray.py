class Solution:
    # DP solution, current max relate with pre max or pre min if cur num is negative
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        pre_max = nums[0]
        pre_min = nums[0]
        res = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min

        return res