class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        nums = list(s)
        self.backtrack(0, nums, res, n)
        res.append(s)
        return res

    def backtrack(self, start, curr, res, n):
        for i in range(start, n):
            if (97 <= ord(curr[i]) <= 122):
                curr[i] = chr(ord(curr[i]) - 32)
                res.append(''.join(curr))
                self.backtrack(i + 1, curr, res, n)
                curr[i] = chr(ord(curr[i]) + 32)

            elif (65 <= ord(curr[i]) <= 90):
                curr[i] = chr(ord(curr[i]) + 32)
                res.append(''.join(curr))
                self.backtrack(i + 1, curr, res, n)
                curr[i] = chr(ord(curr[i]) - 32)

        

            
