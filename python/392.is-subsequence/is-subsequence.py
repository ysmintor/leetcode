class Solution:
    # 针对 follow up 方面，大量求是否是子序列的情况会好很多，关键在于理解 idx 和 start 方面的关系
    # start = d[c][idx]+1总会是越来越大的，在二叉查找时会变小，但后面又通过 d 中对应 index 求值，因此又会变大
    # 想不明白可以用 s=aada t=bbaddaddacc 来模拟这个过程，演算一遍应该是可以理解
    def isSubsequence(self, s: str, t: str) -> bool:
        d = collections.defaultdict(list)
        for i, c in enumerate(t):
            d[c].append(i)
        start = 0
        for c in s:
            idx = bisect.bisect_left(d[c], start)
            if len(d[c]) == 0 or idx >= len(d[c]):
                return False
            start = d[c][idx] + 1
        return True

    # 正常的解决，双指针，如果仅仅是解决一个子序列比较好
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s > len_t:
            return   False
        i=j=0
        while j<len_t and i < len_s:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == len_s

    # Dynamic soltuion dp[i] 代表当前 t[i]位置能够匹配到 s串中最大长度，相应的有递推方程式
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return  True
        if not t:
            return False
        len_s = len(s)
        len_t = len(t)
        if len_s > len_t:
            return   False

        dp = [0]*(len_t+1)
        dp[0] = 0

        for i in range(1, len_t+1):
            index = dp[i-1]
            dp[i] = index+1 if s[index] == t[i-1] else dp[i-1]
            if dp[i] == len_s:
                return True

        return False