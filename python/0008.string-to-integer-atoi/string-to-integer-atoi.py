class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s:
            return 0
        sign = 1
        if s[0] in ('+', '-'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        ans = 0
        for c in s:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break
        ans *= sign
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        return ans