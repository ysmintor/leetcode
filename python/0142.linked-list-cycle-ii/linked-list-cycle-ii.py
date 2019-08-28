# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=finder=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # a loop exists when fast and slow meets
            if slow == fast:
                # slow to cycle begins equals the same distance to head
                while finder != slow:
                    finder = finder.next
                    slow = slow.next
                return finder
        return None