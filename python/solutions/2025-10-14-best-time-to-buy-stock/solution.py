from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        best_buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]> best_buy:
                max_prof = max(max_prof,prices[i] - best_buy)
            best_buy = min(best_buy,prices[i])
        return max_prof
                

        
