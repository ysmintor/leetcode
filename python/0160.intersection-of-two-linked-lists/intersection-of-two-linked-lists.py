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