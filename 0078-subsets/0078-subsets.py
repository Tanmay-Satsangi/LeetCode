class Solution:
    def subsets(self, nums):
        res = []
        self.backtrack(0, nums, [], res)
        return res
    
    def backtrack(self, start, nums, curr, res):
        res.append(list(curr))
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.backtrack(i + 1, nums, curr, res)
            curr.pop()