# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True

        slow = fast = head

        # Find half of the linked list
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = self.reverse_linked_list(slow.next)

        slow = slow.next

        while slow:
            if head.val != slow.val:
                return False

            head = head.next
            slow = slow.next

        return True

    
    def reverse_linked_list(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
