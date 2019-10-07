class Solution:
    # 本题的思路基本上还是BFS套路，另外一种是使用 Disjoint Set(并查集的办法）
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            # empty case
            return 0
        m, n = len(grid), len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                # encounter the first island tag then count and smash island's other part
                if grid[i][j] == '1':
                    island += 1
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        # set to visited
                        grid[row][col] = '0'
                        # check correct range and set 2 to avoid repeat add to stack
                        if row-1 >= 0 and grid[row-1][col] == '1':
                            grid[row-1][col] = 2
                            stack.append((row-1, col))
                        if row+1 < m and grid[row+1][col] == '1':
                            grid[row+1][col] = 2
                            stack.append((row+1, col))
                        if col-1 >= 0 and grid[row][col-1] == '1':
                            grid[row][col-1] = 2
                            stack.append((row, col-1))
                        if col+1 < n and grid[row][col+1] == '1':
                            grid[row][col+1] = 2
                            stack.append((row, col+1))

        return island
