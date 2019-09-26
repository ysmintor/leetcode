class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        length=len(nums)
        for i in range(0, length-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]:
                continue
            self.find_two_sum(nums, i+1, length-1, -nums[i], results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
