class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(0, 0, "", n, res)
        return res

    def backtrack(self, open, close, s, n, res):
        if open == n and close == n:
            res.append(s)
            return 

        if (open < n):
            self.backtrack(open + 1, close, s + "(", n, res)

        if (close < open):
            self.backtrack(open, close + 1, s + ")", n, res)


        