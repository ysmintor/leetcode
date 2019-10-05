# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv
        while intv < length:
            # reset pre and h to start index
            pre, h = res, res.next
            while h:
                # get the two merge head h1 and h2
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                # no need to merge because the `h2` is None since h is None and i > 0
                if i :
                    break

                h2, i = h, intv
                while i and h:
                    h, i = h.next, i -1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the intv
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2

        return res.next
