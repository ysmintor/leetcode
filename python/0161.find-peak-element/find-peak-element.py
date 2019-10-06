class Solution:
    # 使用二分查找的思想，与相邻元素比较，nums[-1] = nums[n] = -∞， nums[-1]指的是 nums[0]前面的元素，nums[n]则是结尾元素后面，说明一定存在峰值
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l