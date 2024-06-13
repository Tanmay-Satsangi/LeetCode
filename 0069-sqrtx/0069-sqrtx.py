#(0 ** 0) = 1 
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 0 #because if x == 0 then return 0. Also for 0 while loop does not run

        while (low <= high):
            mid = (low + high) // 2

            if (mid * mid) <= x:
                ans = mid
                low = mid + 1 #check for greater positive numer
            else:
                high = mid - 1

        return ans