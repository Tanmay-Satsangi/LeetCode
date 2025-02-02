# TC = O(N ^ 2)
# SC = O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        pal_start = pal_max_len = 0

        for i in range(n):
            pal_start1, pal_len1 = self.expand_around_centers(s, i, i) # For odd palindrome
            pal_start2, pal_len2 = self.expand_around_centers(s, i, i + 1) # For Even Palindrome

            if  pal_len1 > pal_max_len:
                pal_start, pal_max_len = pal_start1, pal_len1
            if pal_len2 > pal_max_len:  # Both are must be "if condition" because it's possibility that pal_len1 and pal_len2 both are together greter then pal_mal_len at a time. 
                pal_start, pal_max_len = pal_start2, pal_len2

        return s[pal_start: pal_start + pal_max_len]

    
    def expand_around_centers(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        
        return l + 1, r - l - 1 
