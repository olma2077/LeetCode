var maxProfit = function(prices) {
        let profit = 0
        let long = true
        
        for (let i =1; i < prices.length; i++) {
            if (prices[i-1] < prices[i]) {
                if (long) {
                    profit -= prices[i-1]
                    long = !long
                }
            } else {
                if (!long) {
                    profit += prices[i-1]
                    long = !long
                }
            }
        }
        if (!long) {
            profit += prices[prices.length - 1]
        }    
        return profit
}
