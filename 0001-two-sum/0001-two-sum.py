class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        n = len(nums)
        
        for i in range(len(nums)):
            rem = target - nums[i]
            val = nums[i]

            if (rem in dict1) and (dict1[rem] != i):
                return [i, dict1[rem]]
            else: 
                dict1[nums[i]] = i
        