#m = Number of rows
#n = Numbere of columns

# TC = O(N)
#SC = O(1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #One Way
        # N = m + n - 2  #Number of rows + Number of columns - 2
        # r = m - 1   #Number of rows - 1
        # res = 1
        
        # #Calculate: N
        # #            C
        # #             r
        
        # for i in range(1, r + 1):
        #     res = res * (N - r + i) / i
            
        # return int(res)

        #Another Way(By Bosscoder Academy i.e. Amit Kumar)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):
                    dp[i][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]