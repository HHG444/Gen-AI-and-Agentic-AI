
def maxProfit(self,prices: [int]) -> int:
    maxProfit = 0
    for i in range(len(prices)-1):
        maxProfit += max(prices[i+1]-prices[i],0)
    return maxProfit
prices = [7,6,5,4,3,1,2,9,8,9]
print(maxProfit("self",prices))
#=============================
def maxProfit(prices: [int]) -> int:
    maxProfit = 0
    for i in range(len(prices)-1):
        maxProfit += max(prices[i+1]-prices[i],0)
    return maxProfit
#prices = [7,6,5,4,3,1,2,9,8,9]
#print(maxProfit(prices))