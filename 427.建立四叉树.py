#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m, n = len(grid), len(grid[0])
        presum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + grid[i][j]
        
        def dfs(x0, y0, x1, y1):
            if not (diff := presum[x1][y1] - presum[x1][y0] - presum[x0][y1] + presum[x0][y0]):
                return Node(False, True, None, None, None, None)
            elif diff == (x1 - x0) * (y1 - y0):
                return Node(True, True, None, None, None, None)
            else:
                return Node(True, False, dfs(x0, y0, hx:=(x0 + x1) // 2, hy:=(y0 + y1) // 2),
                                         dfs(x0, hy, hx, y1),
                                         dfs(hx, y0, x1, hy),
                                         dfs(hx, hy, x1, y1))
        return dfs(0, 0, m, n)
        
# @lc code=end

