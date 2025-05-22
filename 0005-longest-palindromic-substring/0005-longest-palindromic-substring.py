class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_max_len = pal_start = 0
        n = len(s)

        for i in range(n):
            # For Odd String
            pal_start1, pal_len1 = self.expand_around_centers(s, i, i)
            pal_start2, pal_len2 = self.expand_around_centers(s, i, i + 1)

            if pal_len1 > pal_max_len:
                pal_max_len, pal_start = pal_len1, pal_start1

            if pal_len2 > pal_max_len:
                pal_max_len, pal_start = pal_len2, pal_start2

        return s[pal_start: pal_start + pal_max_len]

        
    def expand_around_centers(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        return (l + 1, r - l - 1)
