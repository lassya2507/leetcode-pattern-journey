class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prof = 0
        minc = prices[0]
        for i in range(1,len(prices)):
            prof = max(prices[i]-minc,prof)
            minc = min(prices[i],minc)
        return prof




