# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 使用了一个外部的计算判断当前结点奇偶
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        count = 1
        odd_head = ListNode(None)
        even_head = ListNode(None)

        odd_tail = odd_head
        even_tail = even_head
        p = head
        while p:
            # odd case
            if count % 2 == 1:
                odd_tail.next = p
                odd_tail = odd_tail.next
            else:
                even_tail.next = p
                even_tail = even_tail.next
            p = p.next
            count += 1
        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next

    # 直接利用轮换对称性，交替地改变指针下一个位置
    def oddEvenList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_head = odd_tail = head
        even_head = even_tail = head.next

        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next


        odd_tail.next = even_head
        return odd_head

"""
核心实质都是分奇偶开头，然后利用尾插法拼接结点。
"""