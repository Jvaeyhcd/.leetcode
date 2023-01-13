#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#

# @lc code=start
from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.prices = SortedList()
        self.timePriceMap = {}
        self.maxTimestamp = 0


    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePriceMap:
            self.prices.discard(self.timePriceMap[timestamp])
        self.prices.add(price)
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)


    def current(self) -> int:
        return self.timePriceMap[self.maxTimestamp]


    def maximum(self) -> int:
        return self.prices[-1]


    def minimum(self) -> int:
        return self.prices[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

