class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while (i < n):
            corrected_index = nums[i] - 1

            if (nums[i] != nums[corrected_index]):
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if (i != (nums[i] - 1)):
                return nums[i]
            

        