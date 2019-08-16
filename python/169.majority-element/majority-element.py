"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
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