# Binary Search
# TC = O(logN)
# SC = O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        #Remember that there is not 'equal to' sign because it goes to infinite loop
        while (low < high):
            mid = (low + high) // 2

            if nums[mid] > nums[high]:  # if this condition is true then it guranteed that minimum element is present at [mid + 1, high] because mid is greter then the value at high
                low = mid + 1
            else:
                high = mid #there is chance that 'mid' is may be the minimum element so, we cannot neglect mid

        return nums[low] # Low always return the minumum element of rotated sorted array.
                



        # n = len(nums)

        # low = 0
        # high = (n - 1)

        # if nums[low] < nums[high]:
        #     return nums[0]

        # while (low <= high):
        #     mid = (low + high) // 2

        #     if nums[mid] > nums[mid + 1]:
        #         return nums[mid + 1]

        #     #Always minimum element is present in un-sorted part of array.
        #     elif (nums[low] <= nums[mid]): #condition to check the part is sorted
        #         low = mid + 1
        
        #     else:
        #         high = mid - 1

        
        # return -1