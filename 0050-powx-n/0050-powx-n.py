# Edge Case: n can be negative value ?

class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        ans = 1.0

        if nn < 0:
            nn = nn * -1 # To become nn positive

        while nn:
            if nn % 2 == 1:    # If power is odd.
                ans = ans * x
                nn -= 1
            else:
                x = x * x
                nn = nn // 2

        if n < 0:
            ans = 1.0 / ans

        return ans

        