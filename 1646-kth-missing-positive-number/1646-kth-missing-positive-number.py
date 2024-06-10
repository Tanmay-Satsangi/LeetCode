#Binary Search

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        low = 0
        high = (n - 1)

        while(low <= high):
            mid = (low + high) // 2

#Add 1 because range is start from 1 so, at index 0, value 1 is present
# Similarly, at index 1 value 2 is present.

            missing = arr[mid] - (mid + 1) 

            if missing >= k:  #i.e. if kth missing number is present in the range (low, mid)
                high = mid - 1
            else:
                low = mid + 1

        return high + k + 1
