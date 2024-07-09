class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips = 0
        ans = 0
        i = 0
        j = 0
        n = len(nums)

        while (i < n):
            if nums[i] == 0:
                flips += 1

            while (flips > k):
                #Unflip from start
                if nums[j] == 0:
                    flips -= 1
                j += 1
            ans = max(ans, i - j + 1)
            i += 1

        return ans
        