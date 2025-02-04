# 1st Approach: Sort both strings lexicographically using sorted(), then compare them. If they match, return True; otherwise, return False.

# TC = O(N logN)
# SC = O(N) # For list of characters

# return ''.join(sorted(s)) == ''.join(sorted(t))  # sorted() returns a list of characters.

# ------------------------------------------------------------------------------------------

# 2nd Approach
# TC = O(s1 + t1) 
# SC = O(s1 + t1)
# where s1 and t1 are the lengths of string s and t.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
