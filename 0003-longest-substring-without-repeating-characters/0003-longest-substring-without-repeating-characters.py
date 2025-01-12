class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0
        visited = {}
        max_len = 0

        for r in range(n):
            if s[r] in visited and l <= visited[s[r]]:
                l = visited[s[r]] + 1
            else:
                max_len = max(max_len, r - l + 1)
            
            visited[s[r]] = r

        return max_len

