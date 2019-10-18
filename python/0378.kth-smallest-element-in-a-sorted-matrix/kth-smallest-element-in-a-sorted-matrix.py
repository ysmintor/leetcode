from heapq import *
class Solution:
    # 利用大根堆解
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minheap = []
        n = len(matrix)
        for i in range(min(k, n)):  # 当k小于n时，只需遍历前k行
            heappush(minheap, (matrix[i][0], i, 0))  # 堆里的每个元素是（matrix[i][j], i, j）

        counter = 0
        x, i, j = 0, 0, 0
        while counter < k:
            counter += 1
            x, i, j = heappop(minheap)
            if j < n-1:
                heappush(minheap, (matrix[i][j+1], i, j+1))  # 向堆里加入该元素所在行的下一个元素
        return x
    # 利用二分思想处理
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l+r) // 2
            # get count of num less or equal to mid
            cnt = self.search_less_equal(matrix, mid)
            # binary search method
            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return l

    def search_less_equal(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        row, col, res = n-1, 0, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                res += row + 1
                col += 1
            else:
                row -= 1
        return res