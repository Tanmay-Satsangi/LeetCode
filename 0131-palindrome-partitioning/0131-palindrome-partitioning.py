# TC = O(N * (2 ^ N))
# SC = O(2 ^ N)       #Because of recursion tree.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())     #Because 'res' and 'curr' reference to the same array so, and in later code we have to apply operation on curr but not on res so, we have to create DEEP COPY. 

                return 
            
            for j in range(i, len(s)):
                #If string index 'i' to 'j' (Both Include) is Palindrome then, we append in list 'part' and after we call 'j + 1'
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()      #Delete recently add(string), just before 2 lines.
        
        dfs(0)
        return res
                    
        #Code to check the given length is Palindrom or not(l and r both are included)    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
                
            l +=1
            r -= 1
            
        return True