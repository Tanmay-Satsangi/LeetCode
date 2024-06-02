class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        max_sum = 0
        n = len(nums)

        #sum till k
        for i in range(k):
            sums += nums[i]

        l = 0
        r = (k - 1)
        max_sum = sums

        while (r < (n - 1)):
            sums -= nums[l]
            l += 1
            r += 1
            sums += nums[r]

            max_sum = max(max_sum, sums)
        
        return max_sum / k

        


