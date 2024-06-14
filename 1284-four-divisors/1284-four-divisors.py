class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for num in nums:
            x = set()

            sqrt_num = sqrt(num)
            for i in range(1, floor(sqrt_num) + 1):
                if num % i == 0:
                    x.add(i)
                    x.add(num // i)

                if len(x) > 4: 
                    break

            if len(x) == 4:
                res += sum(x)

        return res

