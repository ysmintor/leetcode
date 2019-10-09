class Solution:
    # 这个题目真的是太秀了，用空间换时间，感觉有些像DP的题目，就是左右相乘，这样看是分治来处理，
    # 注意这个题目讲的是输出的数组不计算在空间复杂度内，所以计算过程只依赖常数个空间就可以了
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

    """
    简单想法：对于题目是例子[1, 2, 3, 4]，想求出 3位置结果，我们要知道3位置前的乘积，和后面的乘积，即[1, 2] 和 [4]，所以我们用前缀积，和后缀积记录：

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums[:-1]:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in nums[::-1][:-1]:
            suffix.append(suffix[-1] * num)
        return list([a * b for a, b in zip(prefix, suffix[::-1])])
