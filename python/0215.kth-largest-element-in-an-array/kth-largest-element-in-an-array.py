from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest is (n-k)th smallest one
        k_smallest = len(nums) - k
        return self.find(nums, k_smallest, 0, len(nums) - 1)

    def find(self, nums: List[int], k_smallest: int, left: int, right: int) -> int:
        if left == right:
            # If the list contains only one element, must be the wanted one
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = self.partition(nums, pivot_index, left, right)
        if pivot_index == k_smallest:
            return nums[k_smallest]
        elif pivot_index < k_smallest:
            return self.find(nums, k_smallest, pivot_index + 1, right)
        else:
            return self.find(nums, k_smallest, left, pivot_index - 1)

    def partition(self, nums: List[int], pivot_index: int, left: int, right: int):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index


if __name__ == '__main__':
    so = Solution()
    # ans = so.findKthLargest([3,2,1,5,6,4], 2)
    ans = so.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(ans)
