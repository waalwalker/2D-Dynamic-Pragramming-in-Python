class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # States are: Buying or Selling
        # If Buying the stock: i + 1
        # If Selling the stock: i + 2
        
        dp = {} # Here, key = (i, buying); val = max_profit
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
                
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)
    

# Here the time complexity is O(n)
# And, the memory complexity is alos O(n), and we used caching here.
                