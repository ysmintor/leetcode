# 核心思想是利用回溯法来求解，右括号数据小于左括号时就是合规则的可以继续，也就是第三个 If的判断条件
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left + 1, right)
            if right < left:
                backtrack(S+')', left, right + 1)

        backtrack()
        return ans