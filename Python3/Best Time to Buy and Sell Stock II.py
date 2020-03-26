class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        long = True
        
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                if long:
                    profit -= prices[i-1]
                    long = not long
                else:
                    continue
            else:
                if long:
                    continue
                else:
                    profit += prices[i-1]
                    long = not long
       
        if not long:
            profit += prices[len(prices) - 1]
            
        return profit
