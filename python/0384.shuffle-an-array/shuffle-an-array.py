class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.backup = list(nums)
        self.length = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = list(self.backup)
        return self.array



    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        array = self.array
        for i in range(self.length):
            j = random.randrange(i, self.length)
            # swap random
            array[i], array[j] = array[j], array[i]
        return array





    # Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()