class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        
        low = 0
        high = (n - 1)

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            #Check 1st part is sorted
            if nums[low] <= nums[mid]:
                #check target is present is 1st part
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

        return -1