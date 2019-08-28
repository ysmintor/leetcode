class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums[0] if nums else 0
        return max(self.rob2(nums, 0, length-1), self.rob2(nums, 1, length))

    def rob2(self, nums: List[int],  start: int, end: int)-> int:
        rob, skip = 0, 0
        for money in nums[start:end]:
            rob, skip = skip + money, max(rob, skip)
        return max(rob, skip)


"""
这个题目是 house-robber 的一个延伸问题，主要就是首间和最后一间是相连的，因此不能能够同时要求将这两个打劫了，这时换一种思路，转化为要么包含首间要么包含最后一间，后面的问题其实就是 house-robber 的问题了
"""