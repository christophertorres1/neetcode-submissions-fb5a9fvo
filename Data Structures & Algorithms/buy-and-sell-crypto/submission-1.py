class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = float('inf')
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                profit = price - lowest_price
                max_profit = max(profit, max_profit)
        return max_profit

        
