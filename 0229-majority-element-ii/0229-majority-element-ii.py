# Boyer Moore's Voting Algorithm
#TC = O(N) + O(N)
#SC = O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = num2 = -1, -1
        count1 = count2 = 0
        
        for ele in nums:
            if num1 == ele:
                count1 += 1
            elif num2 == ele:
                count2 += 1
            elif count1 == 0:
                num1 = ele
                count1 = 1
            elif count2 == 0:
                num2 = ele
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1 
        
        #Again traverse the nums and check the num1 and num2 appear more than n / 2 times
        # #WHY AGAIN TRAVERSE: THEN RUN TEST CASE:
        # 1. nums = [3, 2, 3]
        # 2. nums = [1]
        # 3. nums = [1, 2] #This test is not for again traverse concept, but to clear the concept
        
        
        c1 = 0
        c2 = 0
        ans = []
        
        for ele in nums:
            if ele == num1:
                c1 += 1
            elif ele == num2:
                c2 += 1
 
        if c1 > len(nums) // 3:
            ans.append(num1)
        if c2 > len(nums) // 3:
            ans.append(num2)
        return ans
        