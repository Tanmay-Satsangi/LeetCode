class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n2 < n1:
            return self.findMedianSortedArrays(nums2, nums1)
            
        low = 0
        high = n1 # binary search on partition indices, not indices of nums1.

        left = (n1 + n2 + 1) // 2
 
        while(low <= high):
            cut1 = (low + high) // 2
            cut2 = left - cut1

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

            right1 = float('inf') if cut1 == n1 else nums1[cut1]
            right2 = float('inf') if cut2 == n2 else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:  # Count of nums1 and nums2 are even
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
