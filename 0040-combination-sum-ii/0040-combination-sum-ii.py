class Solution:
    #candidate is replaced by variable 'nums' for our convenience
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()
        self.backtrack([], res, nums, target, 0)
        return res

    def backtrack(self, curr, res, nums, rem, start):
        if (rem < 0):
            return 

        if (rem == 0):
            res.append(list(curr))
            return

        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i - 1]):
                continue

            curr.append(nums[i])
            self.backtrack(curr, res, nums, rem - nums[i], i + 1)
            curr.pop()

