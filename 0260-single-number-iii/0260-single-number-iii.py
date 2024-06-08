class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        y = 0
        xor = 0
        n = len(nums)

        for i in range(n):
            xor = xor ^ nums[i]

        setbit = xor & ~(xor - 1)

        for i in range(n):
            if (nums[i] & setbit == 0):
                x = x ^ nums[i]
            else:
                y = y ^ nums[i]

        arr = []
        arr.append(x)
        arr.append(y)

        return arr