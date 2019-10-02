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

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1,2,3]))