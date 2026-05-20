class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculate maximum profit from multiple stock transactions.
        Buy and sell whenever there's a price increase from one day to the next.
      
        Args:
            prices: List of stock prices where prices[i] is the price on day i
          
        Returns:
            Maximum profit achievable from multiple buy-sell transactions
        """
        # Initialize total profit
        total_profit = 0
      
        # Iterate through consecutive price pairs
        for i in range(1, len(prices)):
            # Calculate profit from buying on day i-1 and selling on day i
            daily_profit = prices[i] - prices[i-1]
          
            # Only add positive profits (buy low, sell high on consecutive days)
            if daily_profit > 0:
                total_profit += daily_profit
      
        return total_profit
