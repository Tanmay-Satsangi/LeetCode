# TC = O(N)
# SC = O(N)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        n = len(nums)
        count = 0

        for i in range(n):
            if ((nums[i] + diff) in nums_set and (nums[i] + 2*diff) in nums_set):
                count += 1

        return count


        