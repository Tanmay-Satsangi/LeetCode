# TC = O(log(min(a,b)))

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minm = min(nums)
        maxm = max(nums)

        return self.find_gcd_max_min(maxm, minm)


    def find_gcd_max_min(self, a, b):
        if b == 0:
            return a

        return self.find_gcd_max_min(b, a % b)
