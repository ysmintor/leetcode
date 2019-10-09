class Solution:
    # 主要就是利用到了滑动窗口
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = _sum = sum(nums[0:k])

        for i in range(k, len(nums)):
            _sum = _sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, _sum)
        return max_sum / k
