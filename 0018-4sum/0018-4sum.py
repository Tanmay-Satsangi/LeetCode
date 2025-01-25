# TC = O(Nlogn) + O(N ^ 3) 
# therefore, TC = O(N ^ 3)
# SC = O(1)

# APPROACH: 2 loop + 2 pointer

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        if n < 4:
            return []
        
        nums.sort()
        ans = []
        i = 0
        while i < n:
            j = i + 1
            #rem = target - nums[i]  cannot use in 4 sum try ex: [1, 0, -1, -2, 2] and target = 0
            while j < n:
                left = j + 1
                right = n - 1
                # rem = rem - nums[j] cannot use in 4 sum try ex: [1, 0, -1, -2, 2] and target = 0 because 2nd time this j loop runs we have to again update rem = target - nums[i]
                
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        #increment left(use loop to avoid duplicate values)
                        while left < n and nums[left] == nums[left - 1]:
                            left += 1
                        #increment right(use loop to avoid duplicate values)
                        while right >= 0 and nums[right] == nums[right + 1]:
                            right -= 1
                        
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                    
                #increment j
                j += 1
                while j < n and nums[j] == nums[j - 1]:
                    j += 1
                    
            #increment i
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
            
        return ans
