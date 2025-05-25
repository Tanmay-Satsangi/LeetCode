# TC = O(N)
# SC = O(N)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pt = 0
        nt = 1

        ans = [0] * n

        for i in range(n):
            if nums[i] >= 0:
                ans[pt] = nums[i]
                pt += 2
            else:
                ans[nt] = nums[i]
                nt += 2

        return ans

        