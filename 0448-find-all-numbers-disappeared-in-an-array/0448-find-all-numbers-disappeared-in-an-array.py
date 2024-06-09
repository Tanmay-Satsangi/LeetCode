class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        ans_list = []

        while (i < n):
            corrected_index = nums[i] - 1

            if nums[i] != nums[corrected_index]:
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]

            else: 
                i += 1

        
        #Traverse through index
        for i in range(n):
            if (i + 1) != nums[i]:
                ans_list.append(i + 1)

        return ans_list