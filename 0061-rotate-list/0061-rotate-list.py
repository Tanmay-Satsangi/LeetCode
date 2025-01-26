#TC = O(N) + O(N - N % K) 
#TC = O(N)
#SC = O(1)

#Steps to solve this question
# 1. Count length of the linked list
# 2. next pointer of last node will pointed to head(Create Circular linked list)
# 3. k = len - k
# 4. k = n % k
# 5. next of kth node to None.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #Count number of nodes in Linked list
        curr = head
        n = 1   #Length of the linked list
        while curr.next:
            n += 1
            curr = curr.next
        
        #Create circular singly linked list
        curr.next = head
        
        k = k % n
        k = n - k
        
        newHead = head
        while k != 1:
            newHead = newHead.next
            k -= 1
         
        head = newHead.next
        newHead.next = None
        
        
        return head