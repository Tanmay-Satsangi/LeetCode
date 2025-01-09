class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_element = None

        for ele in nums:
            if maj_element == ele:
                count += 1
            elif count == 0:
                maj_element = ele
                count += 1
            else:
                count -= 1

        return maj_element 
        