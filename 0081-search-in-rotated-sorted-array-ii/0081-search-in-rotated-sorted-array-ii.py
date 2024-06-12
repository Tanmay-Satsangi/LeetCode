class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        low = 0
        high = n - 1

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1

            #check left part is sorted
            elif (nums[low] <= nums[mid]):
                #check condition for target and move low and high pointer
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else: 
                    low = mid + 1

            else: 
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else: 
                    high = mid - 1

        return False