class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0 
        n = len(nums)

        while (j < n):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else: 
                j += 1
        
        return nums
        