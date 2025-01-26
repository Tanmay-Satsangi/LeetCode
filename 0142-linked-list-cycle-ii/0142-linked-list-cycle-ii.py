# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast = slow = entry = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                while entry != slow:
                    entry = entry.next
                    slow = slow.next

                return entry

        return None
