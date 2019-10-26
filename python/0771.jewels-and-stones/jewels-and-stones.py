import collections
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = collections.Counter(S)
        res = 0
        for stone in J:
            res += counter[stone]
        return res

    def numJewelsInStones2(self, J: str, S: str) -> int:
        return sum([S.count(x) for x in J])