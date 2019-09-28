from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)

        def backtrack(permu: List[int], choices: List[int]):
            if len(permu) == length:
                output.append(permu)
                return

            for choice in choices:
                if choice not in permu:
                    permu.append(choice)
                    backtrack(permu.copy(), choices)
                    permu.remove(choice)

        backtrack(list(), nums)
        return output

if __name__ == '__main__':
    so = Solution()
    res = so.permute([1,2,3])
    print(res)