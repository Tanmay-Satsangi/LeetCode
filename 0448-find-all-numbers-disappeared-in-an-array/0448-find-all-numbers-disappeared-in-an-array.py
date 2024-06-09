#Cycle Sort

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_list = []
        i = 0

        while(i < n):
            corrected_index = nums[i] - 1

            #Not Required to check for arr[i] < n becuase range is start from 1 So, 
            #index and value at arr[i] is always less than or equal to last index of array.
            
            #Also, for this, we already decrement the corrected_index by 1 
            if nums[i] != nums[corrected_index]:
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]

            else: 
                i += 1

        for i in range(n):
            if nums[i] != (i + 1):
                ans_list.append(i + 1)

        return ans_list