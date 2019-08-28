# 依然是一道动态规划的题目，直接在给的二维数组里面进行更新，第一个元素由于 i==0,j==0 所以不会进行累计判断，而在边界的部分也是只有一种可能，直接相加
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_1 = len(grid)
        len_2 = len(grid[0])
        for i in range(len_1):
            for j in range(len_2):
                if i != 0 and j != 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                elif i != 0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                elif j != 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
        return grid[i][j]