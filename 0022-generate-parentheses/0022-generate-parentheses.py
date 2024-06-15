class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        self.recursion(res, 0, 0, "", n)
        return res

    
    def recursion(self, res, open, close, s, n):
        if len(s) == n * 2:
            res.append(s)
            return 
        
        if (open < n):
            self.recursion(res, open + 1, close, s + "(", n)
        
        if (open > close):
            self.recursion(res, open, close + 1, s + ")", n)