# To understand the question: https://www.youtube.com/watch?v=UddDgt52h9g
#Little tough question

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_critical_index = None
        first_critical_index = None
        curr_index = 1

        prev = head
        curr = head.next

        res = [-1, -1]

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if prev_critical_index != None:
                    res [0] = min(res[0], curr_index - prev_critical_index) if res[0] != -1 else curr_index - prev_critical_index

                else:
                    first_critical_index = curr_index
                
                prev_critical_index = curr_index

            prev = curr
            curr = curr.next
            curr_index += 1

        
        if prev_critical_index != first_critical_index:
            res[1] = prev_critical_index - first_critical_index

        return res

        