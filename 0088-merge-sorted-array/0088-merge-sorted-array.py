class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        print("last: ", nums1[last])
        m -= 1
        n -= 1

        while (m >= 0 and n >= 0):
            if nums1[m] <= nums2[n]:
                print("nums1[last]: ", last)
                nums1[last] = nums2[n]
                n -= 1
            else:
                nums1[last] = nums1[m]
                m -= 1
            
            last -= 1

            
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1


        