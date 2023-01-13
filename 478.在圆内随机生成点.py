#
# @lc app=leetcode.cn id=478 lang=python3
#
# [478] 在圆内随机生成点
#

# @lc code=start
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center


    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [x + self.x, y + self.y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

