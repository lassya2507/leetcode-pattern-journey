class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i in prices:
            profit = i - min_price
            res = max(res,profit)
            if i<min_price:
                min_price=i
        return res