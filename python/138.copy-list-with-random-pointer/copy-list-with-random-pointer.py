"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = dict()
        p = q = head
        while p:
            dic[p] = Node(p.val, None, None)
            p = p.next
        while q:
            dic[q].next = dic.get(q.next)
            dic[q].random = dic.get(q.random)
            q = q.next
        return dic.get(head)

# 这些主要利用了字典来创建新的元素，然后利用字典来建立 random 的关系，利用 Python 库 from collection import defualtdict
# dic = defaultdict(lambda : Node(None, None, None) 可以实现只遍历一次