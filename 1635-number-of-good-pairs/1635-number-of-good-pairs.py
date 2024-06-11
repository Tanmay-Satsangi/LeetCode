# TC = O(N)
# SC = O(N)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict1 = {}
        res = 0

        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else: 
                res += dict1[num]
                dict1[num] += 1

        return res
