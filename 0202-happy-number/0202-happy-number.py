# https://www.youtube.com/watch?v=ocDwEjRVDAk

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sum_digits_square(n)
        fast = self.sum_digits_square(self.sum_digits_square(n))

        while (slow != fast):
            slow = self.sum_digits_square(slow)
            fast = self.sum_digits_square(self.sum_digits_square(fast))

        return slow == 1
        
    def sum_digits_square(self, n):

        ans = 0

        while(n):
            rem = n % 10
            ans += (rem * rem)
            n = n // 10

        return ans

    
