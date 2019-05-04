class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        BUYING_STATUS = 0
        SELLING_STATUS = 1
    
        profit = 0
        STATUS = BUYING_STATUS
        
        n = len(prices)
        index = 0
        while index < n-1:
            if STATUS == BUYING_STATUS:
                if prices[index] >= prices[index + 1]:
                    index = index + 1
                else:
                    # Buy stock <=> decrease profit
                    profit -= prices[index]
                    STATUS = SELLING_STATUS
            elif STATUS == SELLING_STATUS:
                if prices[index] <= prices[index + 1]:
                        index = index + 1
                        
                        # Corner case
                        if index == n-1:
                            if prices[index - 1] < prices[index]:
                                profit += prices[index]
                            else:
                                profit += prices[index - 1]
                else:
                    # Sell stock <=> increase profit
                    profit += prices[index]
                    STATUS = BUYING_STATUS
        
        return profit