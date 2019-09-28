class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.extreme_insert_idx(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        # find right bound
        right_idx = self.extreme_insert_idx(nums, target, False) - 1
        return [left_idx, right_idx]

    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insert_idx(self, nums: List[int], target: int, leftBound: bool) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (leftBound and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo
