class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = max_count = 0

        for r, char in enumerate(s):
            if char in dic and dic[char] >= l:
                l = dic[char] + 1
            
            dic[char] = r
            max_count = max(max_count, r - l + 1)

        return max_count
        