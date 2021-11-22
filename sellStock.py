class Solution:
    def maxProfit(self, prices: [int]) -> int:
            _min = max(prices)
            _max = 0
            for x in prices:
                if(x < _min):
                    _min = x

                elif (x - _min > _max):
                    _max = x - _min


            return(_max)
