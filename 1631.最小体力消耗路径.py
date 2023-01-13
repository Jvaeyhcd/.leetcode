#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        vis = set()
        while q:
            c, i, j = heappop(q)
            if i == m - 1 and j == n - 1:
                return c
            if (i, j) in vis:
                continue
            vis.add((i, j))
            for ni, nj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis:
                    cur = abs(heights[i][j] - heights[ni][nj])
                    heappush(q, (max(cur, c), ni, nj))
        return -1
# @lc code=end

