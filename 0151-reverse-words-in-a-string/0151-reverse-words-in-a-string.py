# https://www.youtube.com/watch?v=VcBy0s5q2kk

# TC = O(N)
# SC = O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ") #  We have to use the extra space because in Python string are immutable so, we cannot modifty the string in place.

        n = len(words)
        ans = []
        
        for i in range(n - 1, -1, -1):
            if len(words[i]) > 0:
                ans.append(words[i])

        return " ".join(ans)
