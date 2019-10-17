class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]

"""
摇摆数组的定义理解后，想到就是通过排序，从中间分成一个大的一个小的数组，但这样对于有重复的数组会有问题，所以需要从大到小的方式来处理
"""