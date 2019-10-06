def findMissingRanges(self, nums, lower, upper):
    # 一个比较平常的算法，处理起来需要注意边界条件，另外还应该考虑只有一个边界或者没有边界的情况，下面的代码都能够处理
    ans = []
    nums = [lower - 1] + nums + [upper + 1]
    for i in range(0, len(nums) - 1):
        if nums[i] + 2 == nums[i + 1]:
            ans.append(str(nums[i] + 1))
        if nums[i + 1] > nums[i] + 2:
            ans.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
    return ans