class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.backtrack([], nums, res) #No need of start because loop always start from '0'.
        return res

    def backtrack(self, curr, nums, res): #No need o
        if len(curr) == len(nums):
            res.append(list(curr))

        for i in range(len(nums)):
            if nums[i] in curr:
                continue

            curr.append(nums[i])
            self.backtrack(curr, nums, res)
            curr.pop()

        