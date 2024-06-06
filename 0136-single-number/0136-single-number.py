class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0 #because 0 ^ value = value

        for num in nums:
            ans = ans ^ num

        return ans
