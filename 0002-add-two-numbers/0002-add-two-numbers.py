# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        temp = dummy

        while l1 or l2 or carry:
            sums = 0

            if l1:
                sums =+ l1.val
                l1 = l1.next
            
            if l2:
                sums += l2.val
                l2 = l2.next

            sums += carry
            carry = sums // 10
            node = ListNode(sums % 10)
            temp.next = node
            temp = temp.next

        return dummy.next