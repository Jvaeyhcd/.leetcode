#
# @lc app=leetcode.cn id=2406 lang=python3
#
# [2406] 将区间分为最少组数
#

# @lc code=start
from heapq import heappush, heapreplace
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        q = []
        for l, r in intervals:
            if q and l > q[0]:
                heapreplace(q, r)
            else:
                heappush(q, r)
        return len(q)
# @lc code=end

