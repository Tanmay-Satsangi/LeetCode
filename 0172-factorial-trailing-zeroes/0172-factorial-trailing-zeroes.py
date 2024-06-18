# TC = O(logN)
# SC = O(1)

# Approach: The two numbers which are responsible to make trailing zeroes are ' 5 & even number(2, 4, 6, 8)'. 
#             Ex: 5! => 5 * 4 * 3 * 2 * 1 => 120 (Here 5 and 2 are responsible to make '0'). 
#             Ex: 10! => 3628800 (Here 2 zeroes are come due to the 10(5 * 2) and second one 5 * 2)

# But the count of 5 is always less then the even numbers so, we count the divisible of 5 in given variable 'n'


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        while (n != 0):
            n = n // 5
            count += n

        return count

