# https://www.youtube.com/watch?v=m-EBGjwlqIw => To understand the concept and 1st approach
# https://www.youtube.com/watch?v=S6cUjbQuTnE => For Code

from heapq import nlargest, nsmallest
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')

        if (n <= 4):  #because we convert all the three element to 
            return 0
        
        min_element = sorted(nsmallest(4, nums))
        max_element = sorted(nlargest(4, nums))

        for i in range(4):
            res = min(res, max_element[i] - min_element[i])
        return res
        