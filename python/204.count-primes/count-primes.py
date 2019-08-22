class Solution:
    def countPrimes(self, n: int) -> int:
        # boundry check
        if n < 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, n):
            if not prime[i]:
                continue
            for index in range(2*i, n, i) :
                prime[index] = False
        return prime.count(True)
