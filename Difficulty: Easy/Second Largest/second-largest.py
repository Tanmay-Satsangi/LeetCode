#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        maxm = -1
        second_maxm = -1
        n = len(arr)
        
        for i in range(n):
            if (arr[i] > maxm):
                second_maxm = maxm
                maxm = arr[i]
            elif (arr[i] < maxm and arr[i] > second_maxm):
                second_maxm = arr[i]
                
        return second_maxm


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends