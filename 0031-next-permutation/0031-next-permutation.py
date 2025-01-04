class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1

        while n > 0 and nums[n - 1] >= nums[n]:
            n -= 1 
        
        if n == 0:
            return nums.reverse()
        
        i = n - 1
        j = len(nums) - 1

        while nums[i] >= nums[j]:
                j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]

        nums[n:] = nums[n:][::-1]

        