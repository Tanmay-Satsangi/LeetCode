class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        low = 0
        high = n - 1

        nums.sort()
        while (low < high): #no "Equal to" sign because we did not include the pair where i == j
            if (nums[low] + nums[high]) < target:
                count += (high - low)
                low += 1

            else: 
                high -= 1

        return count
            
