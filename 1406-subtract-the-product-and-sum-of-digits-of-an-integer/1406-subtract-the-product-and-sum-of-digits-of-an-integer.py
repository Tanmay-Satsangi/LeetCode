class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0

        string = str(n)

        for s in string: 
            product *= (int(s))
            sums += (int(s))

        res = product - sums
        return res


        