class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                   #ind  
        #prices = [7,1,5,3,6,4] output = 5
                            #ind+1 
        #profit = sell - buy
        max_profit = 0
        buy = prices[0]
        for sell in prices:
            buy = min(sell, buy)
            max_profit = max(max_profit, sell - buy)
        return max_profit
        
        