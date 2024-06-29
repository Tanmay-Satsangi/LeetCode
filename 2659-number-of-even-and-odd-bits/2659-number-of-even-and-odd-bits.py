class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]

        i = 0

        while(i < 31): #Because the postive range of integer is 2 ^ 31 - 1
            if (n & (2 ** i)):
                if i % 2 == 0:
                    ans[0] += 1
                else:
                    ans [1] += 1
            i += 1

        return ans