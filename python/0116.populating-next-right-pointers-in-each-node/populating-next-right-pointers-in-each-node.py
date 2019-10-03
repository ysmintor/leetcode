
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    # 直接用层序遍历时连接，利用了每一层都是满的特点进行计数
    def connect(self, root: 'Node') -> 'Node':
        # check root empty
        if not root:
            return root

        # init queue
        queue = deque()
        queue.append(root)
        pre: Node = None
        # use num to remember current level children
        level, num = 0, 0
        while queue:
            node = queue.popleft()
            if node.left :
                queue.append(node.left)
                queue.append(node.right)
            num += 1
            if num != 1:
                pre.next = node
            # start a new level
            if num == 2 ** level:
                level += 1
                num = 0
            # remember previous node
            pre = node
        return root

    # 非常不错的思路，直接一层一层连接，利用上一层父结点的 next 已经连接的特性
    def connect2(self, root: 'Node') -> 'Node':
        # check root empty
        if not root:
            return root
        node = root
        while node.left:
            pre = node
            # link current level children
            while node:
                node.left.next = node.right
                node.right.next = node.next.left if node.next else None
                node = node.next
            # start link next level children
            node = pre.left
        return root
