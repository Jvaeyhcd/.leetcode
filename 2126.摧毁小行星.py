#
# @lc app=leetcode.cn id=2126 lang=python3
#
# [2126] 摧毁小行星
#

# @lc code=start
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # 贪心算法
        asteroids.sort()
        for x in asteroids:
            if mass >= x:
                mass += x
            else:
                return False
        return True
# @lc code=end

