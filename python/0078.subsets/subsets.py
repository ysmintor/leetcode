from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init an empty set
        output = [[]]
        for num in nums:
            for j in range(len(output)):
                t1 = output[j].copy()
                t1.append(num)
                output.append(t1)
        return output

    # based on binary tree method
    def subsets2(selfs, nums: List[int]) -> List[List[int]]:
        output = []
        size = len(nums)
        def getSubsets(pos: int, out:List[int]):
            output.append(out)
            for i in range(pos, size):
                out.append(nums[i])
                getSubsets(i+1, out.copy())
                out.pop()
        getSubsets(0, [])
        return output

    # bitwise simulation method
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        output = []
        maxLimit = 1 << len(nums)
        def int2set(num: int):
            out = []
            idx = 0
            while num > 0:
                if num & 1 == 1:
                    out.append(nums[idx])
                idx += 1
                num >>= 1
            return out

        for i in range(maxLimit):
            out = int2set(i)
            output.append(out)

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1,2,3]))