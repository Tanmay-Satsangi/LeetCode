#1st APPROACH:
#TC = O((N1 + N2)log(N1 + N2))  #N1 and N2 are the size of nums1 and nums2.
#SC = O(N1 + N2)

#Merge both the array into new list and return 'k - 1'th element.

##2nd APPROACH: BINARY SEARCH
# TC = O(log(min(n1, n2)))  #n1 and n2 are the length of array nums1 and nums2.
# Sc = O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Very Important line because it handle the edge case also Ex: nums1 = [] and nums2 = [2]
        
    # The first array must be the smaller one because we apply binary search on nums1. Keeping the first array smaller optimizes time complexity to O(log(min(n1, n2))) instead of O(log(n1, n2)).

        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        #Apply Binary Search
        low = 0
        high = n1
        
        while low <= high:
            cut1 = (low + high) // 2
            #Divide the array nums1.
            cut2 = (n1 + n2 + 1) // 2 - cut1    #Divide the array nums2.
            
            #Fill left1, left2 & right1, right2
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right1 = float('inf') if cut1 == n1 else nums1[cut1]
            right2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            #Check the proper division of nums1 and nums2 are done or not.
            if left1 <= right2 and left2 <= right1:
                #Check n1 and n2 are odd length or even length.
                if (n1 + n2) % 2 == 0:      #Even length
                    return (max(left1, left2) + min(right1, right2)) / 2.0  #'/' because we want decimal answer.  
                else:
                    return max(left1, left2)
                
            elif left1 > right2:
                #To take lower element in left1 from previous value of left1 so, we decrese the high
                high = cut1 - 1
            else: 
                low = cut1 + 1
                
