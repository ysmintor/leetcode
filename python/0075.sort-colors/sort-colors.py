class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur, red, blue = 0, 0, len(nums)-1
        while cur <= blue:
            if nums[cur] == 0:
                nums[red], nums[cur] = nums[cur], nums[red]
                red += 1
            elif nums[cur] == 2:
                nums[blue], nums[cur] = nums[cur], nums[blue]
                cur -= 1
                blue -= 1
            cur += 1
