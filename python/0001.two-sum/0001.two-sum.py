from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        revers_dict = dict()
        for i,v in enumerate(nums):
            complement = target - v
            if complement in revers_dict:
                return [i, revers_dict[complement]]

            revers_dict[v] = i
        return []