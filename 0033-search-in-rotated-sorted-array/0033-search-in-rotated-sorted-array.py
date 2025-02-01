class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while (low <= high):
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            #Either low to mid is always sorted or mid to high part is always sorted.
            # = is required when the element is not present and low, high and mid pointed to same index.
            if nums[low] <= nums[mid]:  
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
        