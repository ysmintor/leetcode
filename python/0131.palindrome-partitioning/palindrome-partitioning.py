class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        self.dfs(s, [], output)
        return output

    def dfs(self, s: str, stringList:List[str], results: List[List[str]]):
        if len(s) == 0:
            results.append(list(stringList))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            # backtracking part stringList.append -> dfs -> sttringList.pop
            if self.isPalindrome(prefix):
                stringList.append(prefix)
                self.dfs(s[i:], stringList, results)
                stringList.pop()

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
