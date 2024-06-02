class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_element = -1

        for element in nums:
            if maj_element == element:
                count += 1
            elif count == 0:
                maj_element = element
            else:
                count -= 1

        return maj_element
