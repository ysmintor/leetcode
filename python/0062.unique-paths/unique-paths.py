# 这个题目典型的动态规划解法，二维数组就能解决，关键是生成和修改二维数组的时候，刚开始想简单地修改边界值，发现不会
# 另外对于m=1,n=1的情况我觉得是0而不是1，但直接通过测试不知道没有有这种可能
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # make a 2 dimentional grid of n*m
        grid = [[0]*n for _ in range(m)]

        # recursive put value
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[i][j]