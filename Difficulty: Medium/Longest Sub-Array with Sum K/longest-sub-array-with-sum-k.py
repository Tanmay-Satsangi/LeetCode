#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        if n == 0:
            return 0
            
        sums = 0
        maxm = 0
        dict1 = {}
        
        for i in range(n):
            sums += arr[i]
            
            if sums == k:
                maxm = i + 1
            if sums not in dict1:
                dict1[sums] = i
            
            if (sums - k) in dict1:
                maxm = max(maxm, i - dict1[sums - k])
                
        return maxm
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends