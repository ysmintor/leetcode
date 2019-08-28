'''
思路，通过一个字典将对应的转换建立转换规则记录，每一个字符都检查，不存在就建立对应规则，已经有规则是检查是否符合，不符合则退出。
'''

class Solution:
    # 一个字典，最终检查集合元素个数来确定情况
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomor_dict = {}
        for p,q in zip(s,t):
            if not isomor_dict.get(p):
                # p never exist, then remember it replaced one q
                isomor_dict[p] = q
            elif isomor_dict[p] == q:
                continue
            else:
                # p and q not isomporhic
                return False
        return len(set(isomor_dict.keys())) == len(set(isomor_dict.values()))

    # 两个字典，用于双向绑定与验证
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for p,q in zip(s,t):
            if not dict1.get(p) and not dict2.get(q):
                # p never exist, then remember it replaced one q
                dict1[p] = q
                dict2[q] = p
            elif dict1.get(p) == q and dict2.get(q)== p:
                # rule for p and q already exist and bi direct each one
                continue
            else:
                # p and q not isomporhic case
                return False
        return True