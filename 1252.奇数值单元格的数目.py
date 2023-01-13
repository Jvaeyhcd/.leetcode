#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for x, y in indices:
            rows[x] ^= 1
            cols[y] ^= 1
        return (r := sum(rows)) * n + (c := sum(cols)) * m - 2 * r * c
# @lc code=end

