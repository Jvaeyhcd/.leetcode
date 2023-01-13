#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0
        pos = n - 1
        for x in grid:
            i = pos
            while i >= 0:
                if x[i] >= 0:
                    if i + 1 < n:
                        pos = i + 1
                        ans += (n - pos)
                    break
                i -= 1
            if i == -1:
                ans += n
                pos = -1
        return ans
# @lc code=end

