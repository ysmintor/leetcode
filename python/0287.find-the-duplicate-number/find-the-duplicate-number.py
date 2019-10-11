class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=slow=nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        finder=nums[0]
        while True:
            if finder == slow:
                break
            slow = nums[slow]
            finder = nums[finder]
        return finder

"""
此题大概有两中思路，是种是二分思路，找到中间位置，然后去数大于中间元素的个数以决定去除哪一半
还有就是 Floyd 算法，思路还是与0142的题目一样，转换视角，数组中的 index 对应的数当成是指向元素的下一个 Index，如同是静态链表
"""