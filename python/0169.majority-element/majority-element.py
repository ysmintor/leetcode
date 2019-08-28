# 思想是Boyer-Moore Voting Algorithm，大数超过一半，那么可以知道正负想消，必须会是大数还至少多一个计数，只要计数为0时，就更换大数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = None, 0
        for element in nums:
            if count == 0:
                # change majority element
                majority = element
            if element == majority:
                count += 1
            else:
                count -= 1

        return majority