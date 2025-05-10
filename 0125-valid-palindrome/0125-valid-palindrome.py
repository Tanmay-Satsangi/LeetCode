class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while (l < r):
            if not("a" <= s[l] <= "z" or '0' <= s[l] <= '9'): #Special Character at s[l]
                l += 1

            elif not("a" <= s[r] <= "z" or '0' <= s[r] <= '9'): #Special Character at s[r]
                r -= 1

            elif s[l] != s[r]:
                return False
                
            else: 
                l += 1
                r -= 1

        return True
