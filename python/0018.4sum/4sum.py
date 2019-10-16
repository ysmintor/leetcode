class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs = collections.defaultdict(list)
        # 核心还是转化为两数之和，建立两个数的和与对应的两个数的 index
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pairs[nums[i]+nums[j]].append((i, j))

        res = set()

        for pair_sum, pair in pairs.items():
            for a, b in pair:
                if target - pair_sum in pairs:
                    for k,v in pairs[target-pair_sum]:
                        # 如果找到匹配的数对应的四个 index 都不相同，则添加到结果集中，由于是按大小排序，因此可以去重
                        if a != k and a != v and b != k and b != v:
                            res.add(tuple((sorted([nums[i] for i in [a,b,k,v]]))))
        return res

"""
基于处理的办法其实有好几种，这里只是转化为基于2sum的处理办法，由于给的数组里面的数字是可能重复的，因此我们需要使用 index来判断是不是同一个数，避免一个数被使用多次
"""