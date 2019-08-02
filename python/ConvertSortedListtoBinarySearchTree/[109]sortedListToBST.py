"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 solution try to convert List to Array then use 108 solution
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arrayList = []
        while head:
            arrayList.append(head.val)
            head = head.next
        return self.sortedArrayToBST(arrayList)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            midPos = len(nums) // 2
            root = TreeNode(nums[midPos])
            root.left = self.sortedArrayToBST(nums[0:midPos])
            root.right = self.sortedArrayToBST(nums[midPos+1:])
            return root