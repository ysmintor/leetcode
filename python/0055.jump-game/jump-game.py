class Solution:
    # dynamic planning method
    def canJump1(self, nums: List[int]) -> bool:
        length = len(nums)
        reach = 0
        for i in range(length):
            if reach >= length - 1 or i > reach:
                break
            reach = max(reach, i + nums[i])
        return reach >= length - 1

    # greedy method
    def canJump2(self, nums: List[int]) -> bool:
        dp = [0]*len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return True