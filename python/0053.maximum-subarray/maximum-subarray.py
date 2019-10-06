class Solution:
    # 时间复杂度：O(N)
    # 空间复杂度：O(1)
    # DP solution
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            res = max(res, cur_max)

        return res