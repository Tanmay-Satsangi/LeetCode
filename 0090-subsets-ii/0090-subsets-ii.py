class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(0, nums, [], res)
        return res
    
    def backtrack(self, start, nums, curr, res):
        res.append(list(curr))
        
        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i - 1]):
                continue
            curr.append(nums[i])
            self.backtrack(i + 1, nums, curr, res)
            curr.pop()