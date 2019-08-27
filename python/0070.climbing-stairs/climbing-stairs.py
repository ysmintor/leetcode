# 非常典型的递归备忘录 解法
class Solution:
    memo = []

    def climbStairs(self, n: int) -> int:
        self.memo = [0] * n
        return self.climbStep(0, n)

    def climbStep(self, cur: int, step: int) -> int:
        if cur > step:
            return 0
        elif cur == step:
            return 1  # after step one or two at a time to reach final step
        else:
            if self.memo[cur] > 0:
                return self.memo[cur]

            self.memo[cur] = self.climbStep(cur + 1, step) + self.climbStep(cur + 2, step)
            return self.memo[cur]