import re
class Solution:
    # 可以计数的方式处理，当然最简单就是用正则匹配来处理
    def checkRecord(self, s: str) -> bool:
        return  not re.search("A.*A|LLL", s)