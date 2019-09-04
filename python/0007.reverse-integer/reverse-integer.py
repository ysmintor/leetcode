class Solution:
    def reverse(self, x: int) -> int:
        # 核心思想还是用一个大于32位容器去装翻转数字
        sign = -1 if  x < 0 else 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        return sign * ans if ans <= 0x7fffffff else 0
