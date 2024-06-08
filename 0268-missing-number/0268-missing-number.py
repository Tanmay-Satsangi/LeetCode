#Cycle Sort

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while (i < n):
            corrected_index = nums[i]

            if nums[i] < n and nums[i] != nums[corrected_index]:
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]

            else: 
                i += 1

        for i in range(n):
            if i != nums[i]:
                return i
        return n


    
        