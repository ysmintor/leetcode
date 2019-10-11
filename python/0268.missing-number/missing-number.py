class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, value in enumerate(nums):
            missing ^= i^value
        return missing

    def mssingNumber2(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
"""
这题属于脑精急转弯的题，主要还是需要分析题目，是0-n 之间的数，连接数字可以用高斯求和函数
另外则是利用异或两次相同数，即自身与自身异或抵消了，而且 index 差了最后的len(nums），所以初始值就设置为它
这种题可真有些阴，要是面试心态不好没想到。。。
"""