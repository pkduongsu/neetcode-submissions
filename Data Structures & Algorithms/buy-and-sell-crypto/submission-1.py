class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            currentProf = prices[r] - prices[l]
            if currentProf > 0:
                res = max(res, currentProf)
            else: 
                l = r

            r += 1


        return res
            

