# TC = O(logN)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0

        while (n):
            digit = n % 10
            product *= digit
            sums += digit
            n = n // 10

        res = product - sums

        return res

        


        