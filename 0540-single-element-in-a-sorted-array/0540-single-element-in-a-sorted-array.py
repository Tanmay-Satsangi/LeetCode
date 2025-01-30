# nums[mid ^ 1] returns the index of the paired instance of a repeated element.

# If mid points to the first instance, mid ^ 1 gives the second instance.
# If mid points to the second instance, mid ^ 1 gives the first instance.
# When a single (non-repeating) element appears in the array, the indexing pattern shifts:

# Without a single element: First instance at even index, second instance at odd index.
# With a single element: First instance at odd index, second instance at even index, breaking the pattern.

# TC = O(logN)
# SC = O(N)

# TechDose(For Concept): https://www.youtube.com/watch?v=nMGL2vlyJk0
# Refer Striver video for code implementation.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0
        high = n - 2 # We set high = n - 2 to avoid an index out of range error if the single element is at the last index (edge case).

        while (low <= high):
            mid = (low + high) // 2
    
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid - 1

        return nums[low]
