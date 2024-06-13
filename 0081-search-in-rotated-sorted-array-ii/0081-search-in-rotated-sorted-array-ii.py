class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        low = 0
        high = (n - 1)

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            #Two line change as compared to LC: 33 (Search in Rotated Sorted Array)
            # 1. Add below if condition
            # 2. after this if convert 'if' to 'elif'
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1

            #Check 1st part is sorted
            #Remember there is equal to sign TEST CASE: [3, 1] and target = 1
            elif nums[low] <= nums[mid]:
                #check target is present in 1st part
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            #If 1st part is not sorted then definetely 2nd part is sorted.
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
        