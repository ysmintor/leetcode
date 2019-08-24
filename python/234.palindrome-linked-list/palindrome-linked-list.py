# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # empty or one element case
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        last, pre = slow.next, head
        # reverse left half linked list
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp
        slow = slow.next
        while slow:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
