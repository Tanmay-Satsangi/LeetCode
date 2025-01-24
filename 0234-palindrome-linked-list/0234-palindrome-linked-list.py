# TC = O(N/2) + O(N/2)
# N/2 -> to find middle of linked list
# N/2 -> to reverse the half linked list(slow.next to last)
# SC = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        #Find middle of linked list
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the half Linked list and slow.next point to the half linked list
        slow.next = self.reverseLinkedList(slow.next)
        
        #Move slow to right half
        slow = slow.next
        
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
    
    #Function to reverse the half linked list.
    def reverseLinkedList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
        