class Solution:
    # 解法有很多，从空间 O(n)开始采用同一思路做到 O(1)的话，需要额外设置变量保存，会变得更加复杂，另外这题有比较多的解法，掌握的话非常不错
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start:int, end:int, s:List[int]):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        n = len(nums) - 1
        k = k % len(nums)


        reverse(0, n-k, nums)
        reverse(n-k+1, n, nums)
        reverse(0, n, nums)
        return nums