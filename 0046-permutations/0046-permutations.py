class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.backtrack([], res, nums)
        return res

    def backtrack(self, curr, res, nums):
        if len(curr) == len(nums):
            res.append(list(curr))
            return

        for i in range(len(nums)):
            if nums[i] in curr:
                continue

            curr.append(nums[i])
            self.backtrack(curr, res, nums)
            curr.pop()