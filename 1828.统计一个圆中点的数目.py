#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#

# @lc code=start
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [0] * n
        for i, (x1, y1, r) in enumerate(queries):
            cnt = 0
            for x, y in points:
                dx = x1 - x
                dy = y1 - y
                if dx * dx + dy * dy <= r * r:
                    cnt += 1
            ans[i] = cnt
        return ans
# @lc code=end

