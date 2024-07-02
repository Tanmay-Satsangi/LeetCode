#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        ans = 0
        sums = 0
        dict1 = {}
        
        for i in range(n):
            sums += arr[i]
            if (sums == 0):
                ans = i + 1
            else:
                if sums in dict1:
                    ans = max(ans, i - dict1[sums])
                else:
                    dict1[sums] = i
                    
        return ans
                


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends