# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy_head = ListNode(None)
        dummy_head.next = head
        pre, cur = dummy_head, head
        while cur:
            if cur.val == val:
                pre.next =cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return dummy_head.next
