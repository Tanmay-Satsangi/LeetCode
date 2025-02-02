# TC = O(N * M) Where M = length of the shortest string and N = Number of string.
# SC = O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]

        for i, ch in enumerate(first_string):
            for others in strs[1:]:
                if i >= len(others) or ch != others[i]:
                    return first_string[:i]

        return first_string 
        