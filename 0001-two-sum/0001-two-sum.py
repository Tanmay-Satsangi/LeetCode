class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict_nums = {}

        for i in range(n):
            rem = target - nums[i]

            if rem in dict_nums:
                return [dict_nums[rem], i]
            else:
                dict_nums[nums[i]] = i
        