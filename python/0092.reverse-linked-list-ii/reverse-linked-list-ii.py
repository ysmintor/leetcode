# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        pre = dummy
        dummy.next = head
        for _ in range(m-1):
            # find the previous postion of first reversed element
            pre = pre.next

        cur = pre.next

        for _ in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return dummy.next
