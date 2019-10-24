class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        skip = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                # nums[i] is zero, then increase skip
                skip += 1
            elif skip != 0:
                # none zero jump skip step forward
                nums[i-skip] = nums[i]
        for j in range(-skip, 0):
            nums[j] = 0