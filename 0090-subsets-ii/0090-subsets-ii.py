class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        self.backtrack(0, [], nums, res)
        return res

    def backtrack(self, start, curr, nums, res):
        res.append(list(curr))

        for i in range(start, len(nums)):
            if (i > start and nums[i - 1] == nums[i]):
                continue

            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums, res)
            curr.pop()

