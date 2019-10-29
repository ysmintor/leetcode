class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 数据规模与记忆化
        n, memo = len(piles), dict()

        s = [0]*(n+1)
        # s[i] 表示第 i 堆石子到最后一堆石子的总石子数
        for i in range(n-1, -1, -1):
            s[i] = s[i+1] + piles[i]

        # dfs(i, M) 表示从第 i 堆石子开始取，最多能取 M 堆石子所能得到的最优值
        def dfs(i:int, M:int):
            # 如果已经搜索过，直接返回
            if (i, M) in memo:
                return memo[(i, M)]
            # 溢出拿不到任何石子
            elif i > n:
                return 0
            # 如果剩余堆数小于等于 2M， 那么可以全拿走
            elif i + 2*M >= n:
                return s[i]

            # 枚举拿 x 堆的最优值
            best = 0
            for x in range(1, 2*M+1):
                # 剩余石子减去对方最优策略
                best = max(best, s[i] - dfs(i+x, max(x, M)))
            # 记忆化
            memo[(i, M)] = best
            return best
        return dfs(0, 1)