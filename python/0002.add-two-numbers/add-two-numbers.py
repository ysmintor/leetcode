# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur_l1 = l1
        cur_l2 = l2
        head = ListNode(None)
        cur_node = head
        while (cur_l1 is not None) and (cur_l2 is not None):
            s = cur_l1.val + cur_l2.val + carry
            cur_node.next = ListNode(s % 10)
            carry = s // 10

            cur_node = cur_node.next
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next

        if cur_l1 is None:
            cur_l1 = cur_l2

        while cur_l1 is not None:
            s = cur_l1.val + carry
            cur_node.next = ListNode(s % 10)
            carry = s // 10

            cur_node = cur_node.next
            cur_l1 = cur_l1.next

        if carry == 1:
            cur_node.next = ListNode(1)

        return head.next