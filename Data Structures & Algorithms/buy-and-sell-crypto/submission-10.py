class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            # while we have a profit on the trade (not negative val - price difference is greater than 0)
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)

            # if we don't have profit on this trade condition, we found a right value that is less than our left value, and thus a new minium, which we can set our buy price to left
            else:
                left = right

        return max_profit
