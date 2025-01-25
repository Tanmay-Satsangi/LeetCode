# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = dummy

        #Count total number of nodes
        count = 0 
        curr = head
        
        while curr:
            count += 1
            curr = curr.next

        #Reverse list in group of size k
        while count >= k:
            curr = prev.next
            nxt = curr.next

            for i in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            prev = curr
            count -= k

        return dummy.next


        
