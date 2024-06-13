#(0 ** 0) = 1 


class Solution:
    def mySqrt(self, x: int) -> int:
        #If x == 0, then we have to return 0 because 0 ** 0 is 1. then it does not works for 0.
        if (x == 0):
            return 0

        low = 1
        high = x

        while (low <= high):
            mid = (low + high) // 2

            if (mid * mid) <= x:
                ans = mid
                low = mid + 1 #check for greater positive numer
            else:
                high = mid - 1

        return ans