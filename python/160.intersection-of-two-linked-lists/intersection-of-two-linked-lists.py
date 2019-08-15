"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A: a1 → a2 ↘ c1 → c2 → c3 ↗
B: b1 → b2 → b3

begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null. The linked lists must retain their original structure after the function returns. You may assume there are no cycles anywhere in the entire linked structure. Your code should preferably run in O(n) time and use only O(1) memory.

Credits:Special thanks to @stellari for adding this problem and creating all test cases.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # solution one no trick, deal to the same length of A and B, then compare their elements
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # save two list head
        p1, p2 = headA, headB

        lenA = 0
        while p1:
            lenA += 1
            p1 = p1.next

        lenB = 0
        while p2:
            lenB += 1
            p2 = p2.next

        if lenA > lenB:
            # change to let listA shorter than listB
            temp = headA
            headA = headB
            headB = temp

        for _ in range(abs(lenB - lenA)):
            headB = headB.next

        while headA is not headB:
            headA = headA.next
            headB = headB.next

        return headA

    # with trick to detect
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa