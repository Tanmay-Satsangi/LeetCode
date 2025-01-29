class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        len_g = len(g)
        len_s = len(s)

        g.sort()
        s.sort()

        l = 0
        r = 0

        while (l < len_g and r < len_s):
            if g[l] <= s[r]:
                l += 1
            r += 1

        return l
