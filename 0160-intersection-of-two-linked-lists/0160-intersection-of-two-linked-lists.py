# TC = O(2M) M is maximum length linked list out of 2 linked list.
# SC = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1 = headA
        d2 = headB

        while d1 != None or d2 != None:
            if d1 == d2:
                return d1

            d1 = d1.next if d1 else headB
            d2 = d2.next if d2 else headA

        return None