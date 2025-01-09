# Boyer Moore's Voting Algorithm
#TC = O(N) + O(N)
#SC = O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1 = None
        nums2 = None

        count1 = 0
        count2 = 0

        for ele in nums:
            if nums1 == ele:
                count1 += 1
            elif nums2 == ele:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                nums1 = ele
            elif count2 == 0:
                count2 += 1
                nums2 = ele
            else:
                count1 -= 1
                count2 -= 1

        c1 = 0
        c2 = 0

        for ele in nums:
            if ele == nums1:
                c1 += 1
            elif ele == nums2:
                c2 += 1

        ans = []
        if c1 > len(nums) / 3:
            print("c1")
            ans.append(nums1)
        if c2 > len(nums) / 3:
            print("c2")
            ans.append(nums2)

        return ans

