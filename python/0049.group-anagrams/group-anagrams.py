from typing import List
import collections
# sorted 这个函数有意思
class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == '__main__':
    so = Solution()
    res = so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)