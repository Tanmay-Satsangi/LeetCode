# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        curr = head.next
        sums = 0
        
        # while curr.val == 0:
        #     curr = curr.next
            
        while curr:
            if curr.val != 0:
                sums += curr.val
            else:
                temp.next = ListNode(sums)
                sums = 0
                temp = temp.next
            curr = curr.next
            
        return dummy.next