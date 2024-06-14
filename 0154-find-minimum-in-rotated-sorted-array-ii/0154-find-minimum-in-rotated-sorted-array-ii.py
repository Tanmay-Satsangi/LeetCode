#This question is almost same as LC: 153 but there is 2 changes
# Add if condition 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        #Remember that there is not 'equal to' sign because it goes to infinite loop
        while (low < high):
            mid = (low + high) // 2

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1

            elif (nums[mid] > nums[high]):
                low = mid + 1

            else:
                high = mid

        return nums[low]
