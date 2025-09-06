class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)

        for i in range(n):
            rem = target - nums[i]

            if rem in dic:
                return [dic[rem], i]
            else:
                dic[nums[i]] = i

                