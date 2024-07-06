class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = []
        right = []
        
        l_max = height[0]
        r_max = height[n - 1]
        ans = 0
        
        #for left list
        for i in range(n):
            l_max = max(l_max, height[i])
            left.append(l_max)
            
        #for right list    
        for i in range(n - 1, -1, -1):
            r_max = max(r_max, height[i])
            right.append(r_max)
            
        right.reverse()
            
        #Calculate final ans
        for i in range(n):
            temp = min(left[i], right[i]) - height[i]
            ans += temp
            
        return ans