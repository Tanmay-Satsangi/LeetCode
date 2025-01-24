# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1 = headA
        d2 = headB

        # When d1 and d2 are not null
        while d1 != None or d2 != None:
            if d1 == d2:
                return d1

            if d1 != None:
                d1 = d1.next
            else:
                d1 = headB

            if d2 != None:
                d2 = d2.next
            else:
                d2 = headA

        return None
