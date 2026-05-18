from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # 0
    print(sol.maxProfit([1, 2]))              # 1
