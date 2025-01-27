class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n < 3:
            return [] 

        nums.sort()

        i = 0
        ans = []
        
        while (i < n):
            left = i + 1
            right = n - 1

            while (left < right):
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while (left < n and nums[left] == nums[left - 1]):
                        left += 1

                    while (right >= 0) and nums[right] == nums[right + 1]:
                        right -= 1

                elif sums < 0:
                    left += 1

                else: 
                    right -= 1

            i += 1
            while (i < n and nums[i] == nums[i - 1]):
                    i += 1

        return ans
