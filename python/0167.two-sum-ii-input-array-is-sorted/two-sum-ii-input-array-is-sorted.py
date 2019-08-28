class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = 0, len(numbers) -1
        while index1 < index2:
            sum_index = numbers[index1] + numbers[index2]
            if sum_index == target:
                return [i+1 for i in (index1, index2)]
            elif sum_index > target:
                index2 -= 1
            else:
                index1 += 1