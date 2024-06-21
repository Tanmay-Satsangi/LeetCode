class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        num = 0
        j = 0
        ans = 0
        n = len(nums)

        for i in range(n):
            if (num & nums[i] != 0):
                while (num & nums[i] != 0):
                    #keep removing number from start
                    num = num ^ nums[j]
                    j += 1

            num = num | nums[i]
            ans = max(ans, i - j + 1)

        return ans