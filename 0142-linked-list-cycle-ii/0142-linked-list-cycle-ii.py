# TC = O(2N)
# SC = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = fast = entry = head
        
        #To check their is a loop is exist.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            #To find the entry point of the loop.
            if slow == fast:
                while entry != slow:
                    slow = slow.next
                    entry = entry.next
                    
                return entry
        return None