def maxProfit(self,prices = [int]) -> int:
    maxp = set()
    for n in prices:
            m = prices.index(n)+1
            o = prices.index(n)
            if (m > o):
                trap = m - o
                print('transaction price',trap)
                maxp.add(trap)
    print(sum(maxp))
    
print(maxProfit("self",prices = [7,1,5,5,6,4]))