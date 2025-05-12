class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        res = 0
        gap = float('inf')

        nums.sort()

        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while (l < r):
                sums = nums[i] + nums[l] + nums[r]
                ngap = abs(target - sums)

                if (sums < target):
                    l += 1
                    if ngap < gap:
                        res = sums
                        gap = ngap

                elif (sums > target):
                    r -= 1
                    if ngap < gap:
                        res = sums
                        gap = ngap

                else:
                    return sums

        return res

                    

