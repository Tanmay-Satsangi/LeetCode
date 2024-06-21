class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the numbers to handle duplicates
        self.backtrack([], nums, [False] * len(nums), res)
        return res

    def backtrack(self, curr, nums, used, res):
        if len(curr) == len(nums):
            res.append(list(curr))
            return

        for i in range(len(nums)):
            # Skip used numbers or duplicates
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue

            curr.append(nums[i])
            used[i] = True
            self.backtrack(curr, nums, used, res)
            curr.pop()
            used[i] = False



        # num = nums[:]
        # res = []
        # self.recursion(num, 0, len(num), res)
        # return res
        # res = []
        
        # nums.sort()
        # self.backtrack([], res, nums)
        # return res

    # def backtrack(self, curr, res, nums):
    #     if (len(curr) == len(nums)):
    #         res.append(list(curr))

    #     else:
    #         for i in range(len(nums)):
    #             if (nums[i] in curr) or (i > 0 and nums[i] == nums[i - 1]):
    #                 continue

    #             curr.append(nums[i])
    #             self.backtrack(curr, res, nums)
    #             curr.pop()

    # def recursion(self, num, i, j, res):
    #     if i == j:
    #         res.append(num[:])
    #         return
    #     seen = set()
    #     for k in range(i, j):
    #         if num[k] not in seen:  # Check if num[k] is already seen at current level
    #             seen.add(num[k])
    #             num[i], num[k] = num[k], num[i]
    #             self.recursion(num, i + 1, j, res)
    #             num[i], num[k] = num[k], num[i]  # Swap back to restore original order



        