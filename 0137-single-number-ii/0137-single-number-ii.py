# // https://www.youtube.com/watch?v=Nt920vgqXyE
# // TC = O(N)
# // SC = O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            sum = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    sum += 1

            sum %= 3

            if sum != 0:
                ans |=  (sum << i)

            if ans >= 2**31:
                ans -= 2**32

        return ans
