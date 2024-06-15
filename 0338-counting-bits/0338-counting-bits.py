# https://www.youtube.com/watch?v=awxaRgUB4Kw
# If n == even then the number of 1's in n is same as n // 2
# If n == odd then the number of 1's in n is one greater then n // 2

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(n + 1):
            ans[i] = ans[i // 2] + i % 2

        return ans