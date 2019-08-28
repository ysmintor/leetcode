class Solution:
    # normal process
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        res = n / 2**power
        while res >= 1:
            if res == 1:
                return True
            else:
                power += 1
            res = n / 2 **power
        return False

    # bit operation
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n - 1)
