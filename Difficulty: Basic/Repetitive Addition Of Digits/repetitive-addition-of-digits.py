#User function Template for python3

class Solution:
    def singleDigit(self, N):
    	#code here 
    	
    	if (N == 0):
    	    return 0
    	    
        elif ( N % 9 == 0):
            return 9
            
        else:
            return N % 9


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.singleDigit(N)
        print(ans)
# } Driver Code Ends