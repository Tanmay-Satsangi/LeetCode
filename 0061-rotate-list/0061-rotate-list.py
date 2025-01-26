# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        n = 1

        while curr.next:
            n += 1
            curr = curr.next

        curr.next = head 

        k = k % n
        k = n - k - 1

        newHead = head

        while k:
            newHead = newHead.next
            k -= 1

        head = newHead.next
        newHead.next = None

        return head