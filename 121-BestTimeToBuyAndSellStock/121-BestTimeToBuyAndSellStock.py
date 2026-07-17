# Last updated: 17/07/2026, 15:01:57
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit