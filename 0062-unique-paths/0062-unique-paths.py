#m = Number of rows
#n = Numbere of columns

# TC = O(N)
#SC = O(1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2  #Number of rows + Number of columns - 2
        r = m - 1   #Number of rows - 1
        res = 1
        
        #Calculate: N
        #            C
        #             r
        
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
            
        return int(res)