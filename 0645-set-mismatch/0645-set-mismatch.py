class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans_list = []
        i = 0
        n = len(nums)

        while (i < n):
            corrected_index = nums[i] - 1

            if nums[i] != nums[corrected_index]:
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]

            else: 
                i += 1

        for i in range(n):
            if (i + 1) != nums[i]:
                ans_list.append(nums[i])
                ans_list.append(i + 1)

        return ans_list
        