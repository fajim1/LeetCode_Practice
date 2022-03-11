class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        
        right = 1
        
        profit = 0
        
        while right < len(prices):
            print(left,right)
            if prices[right]-prices[left] < 0:
                
                left = right
                right +=1
                
            else:
                
                if profit < prices[right]-prices[left]:
                    profit = prices[right]-prices[left]
                
                right += 1
                
        
        return(profit)
                
        
        
        
        