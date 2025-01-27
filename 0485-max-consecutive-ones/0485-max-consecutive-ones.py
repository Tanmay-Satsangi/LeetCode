class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        
        curr_ones = 0
        max_ones = 0

        for i in range(n):
            if nums[i] == 1:
                curr_ones += 1
                max_ones = max(curr_ones, max_ones)
            else:
                curr_ones = 0

        return max_ones
