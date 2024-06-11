# Binary Search 
# TC = O(logN)
# SC = O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            #Check left part is sorted 
            if (nums[low] <= nums[mid]):
                #Check condition for target and move low and high pointer
                if (nums[low] <= target and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else: 
                    high = mid - 1

        return -1
