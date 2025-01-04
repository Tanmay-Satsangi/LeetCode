class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        
        #find the element which have next element is not greater
        while n > 0 and nums[n - 1] >= nums[n]:
            n -= 1
         
       #if traverse the whole array is descending order. 
        if n == 0:
            nums.reverse()
            return nums
        
        i = n - 1
        j = len(nums) - 1  
        
        #find the element that is greater than non descending element.
        while nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]    
        
        # reverse the array from non - descending element to last element 
        l, r = n, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        return nums
        
        