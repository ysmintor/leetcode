# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # none recursive method
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            tmp = new_head
            new_head = head
            head = head.next
            new_head.next  = tmp
        return new_head

    # recursive method
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret