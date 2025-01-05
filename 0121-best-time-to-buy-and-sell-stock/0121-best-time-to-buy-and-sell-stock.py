class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        minsofar = prices[0]
        max_profit = 0

        for i in range(1, n):
            profit = prices[i] - minsofar
            max_profit = max(max_profit, profit)
            minsofar = min(minsofar, prices[i])

        return max_profit
