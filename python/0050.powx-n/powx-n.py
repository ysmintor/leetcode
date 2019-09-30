class Solution:
    # 注意学习快速容幂乘
    def myPow(self, x: float, n: int) -> float:
        # deal with negative case
        if n < 0:
            x = 1/x
            n = -n

        tmp = x
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //=2
        return ans