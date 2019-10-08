class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return [num for num, times in count.most_common(k)]

if __name__ == '__main__':
    so = Solution