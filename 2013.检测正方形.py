#
# @lc app=leetcode.cn id=2013 lang=python3
#
# [2013] 检测正方形
#

# @lc code=start
import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.map = collections.defaultdict(lambda:collections.defaultdict(lambda:0))


    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[x][y] += 1


    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        if x not in self.map:
            return 0
        for row, rowCnts in self.map.items():
            if row != x:
                d = row - x
                ans += rowCnts[y] * self.map[x][y + d] * rowCnts[y + d]
                ans += rowCnts[y] * self.map[x][y - d] * rowCnts[y - d]

        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

