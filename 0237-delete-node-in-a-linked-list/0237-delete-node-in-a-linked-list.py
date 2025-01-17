# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # We use node.next.val because the question specifies that the node to be deleted is not the last node in the linked list.
        node.val = node.next.val
        node.next = node.next.next
        