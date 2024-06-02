class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums)) #To remove duplicate
        n = len(nums)
        first_largest = sec_largest = third_largest = float('-inf')

        for i in range(n):
            if first_largest < nums[i]:
                third_largest = sec_largest
                sec_largest = first_largest
                first_largest = nums[i]

            elif sec_largest < nums[i]:
                third_largest = sec_largest
                sec_largest = nums[i]

            elif third_largest < nums[i]:
                third_largest = nums[i]

        return first_largest if third_largest == float('-inf') else third_largest