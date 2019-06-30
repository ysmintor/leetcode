# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:\
#     nums1 = [1, 3]
#     nums2 = [2]
#
#     The median is 2.0
#
# Example 2:
#     nums1 = [1, 2]
#     nums2 = [3, 4]
#
#     The median is (2 + 3)/2 = 2.5
from typing import List
"""
这个题目限制是两个有序的数组，而我在思考的过程中认为是要通过贪心法来求解，但要 log 级的算法，好像必须要折半法来分解，查看解答后确实如此。
关键是在递归过程中首先要保证划分的性质，1.两边的数要相同，2.左边最大的比右边最小的都要小
在[imin, imax]的区间去搜索i的合适位置，利用性质有就对应的 j,再来判断是否符合第2条性质，不符合就调整搜索区间，这个区间以折半的形式来减少，当
然这是最好的情况下，退化时是线性的减少
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            # to ensure m <= n
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m+n+1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1 # i is too small, increase it
            elif i > 0 and nums2[j] < nums1[i-1]:
                imax = i - 1 # i is too large, decrease it
            else:
                # i is perfect
                if i==0: max_of_left = nums2[j-1]
                elif j==0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left

                if i== m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
        return 0.0
