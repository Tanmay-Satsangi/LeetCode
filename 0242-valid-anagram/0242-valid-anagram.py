# 1st Approach: Sort both strings lexicographically using sorted(), then compare them. If they match, return True; otherwise, return False.

# TC = O(N logN)
# SC = O(N) # For list of characters

# return ''.join(sorted(s)) == ''.join(sorted(t))  # sorted() returns a list of characters.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict