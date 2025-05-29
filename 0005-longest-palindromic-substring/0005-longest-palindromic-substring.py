class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_start = pal_max_len = 0
        n = len(s)

        for i in range(n):
            pal_start1, pal_len1 =  self.expand_around_centers(s, i, i)
            pal_start2, pal_len2 = self.expand_around_centers(s, i, i + 1)

            if pal_max_len < pal_len1:
                pal_start, pal_max_len = pal_start1, pal_len1
            if pal_max_len < pal_len2:
                pal_start, pal_max_len = pal_start2, pal_len2

        return s[pal_start:pal_start + pal_max_len]

    def expand_around_centers(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        return l + 1, r - l - 1