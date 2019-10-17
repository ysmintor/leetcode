class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = two = float('inf')
        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True
        return False

"""
大概会用三个变量去依次判断，没想到只用两个变量就可以，这里关键是小于等于时都要进行滑动。因此这个题目感觉是考一个滑动容器的概念。
"""