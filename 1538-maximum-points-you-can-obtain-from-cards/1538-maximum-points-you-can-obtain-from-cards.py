class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sums = sum(cardPoints[0: k])
        sums = 0
        for i in range(k):
            sums += cardPoints[i]

        n = len(cardPoints)

        low = k - 1
        high = n - 1
        ans = sums

        while (low >= 0):
            sums = sums - cardPoints[low] + cardPoints[high]
            low -= 1
            high -= 1
            ans = max(ans, sums)

        return ans