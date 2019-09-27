# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(None)
        dummyHead.next = head
        q = pre = dummyHead
        # find the n-th position from start
        for _ in range(n):
            q = q.next

        while q.next:
            q = q.next
            pre = pre.next

        pre.next = pre.next.next
        return dummyHead.next