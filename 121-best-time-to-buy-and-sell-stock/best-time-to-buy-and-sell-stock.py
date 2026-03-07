class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        size = len(prices)
        i,j = 0,1
        while(j<size):
            if(prices[j] > prices[i]):
                maxp = max(maxp, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return maxp