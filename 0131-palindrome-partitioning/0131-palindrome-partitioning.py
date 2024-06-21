class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(0, [], res, s)
        return res

    def backtrack(self, i, part, res, s):
        if i == len(s):
            res.append((part.copy()))
            return 

        for j in range(i, len(s)):
            if self.is_palindrome(i, j, s):
                part.append(s[i: j + 1])
                self.backtrack(j + 1, part, res, s)
                part.pop()
            
    def is_palindrome(self, l, r, s):
        while(l < r):
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
