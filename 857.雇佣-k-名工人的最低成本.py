#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        pairs = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        ans = 0xf3f3f3f3f3
        total_q = 0
        pq = []

        for q, w in pairs[:k-1]:
            total_q += q
            heappush(pq, -q)
        for q, w in pairs[k-1:]:
            total_q += q
            heappush(pq, -q)
            ans = min(ans, w / q * total_q)
            total_q += heappop(pq)
        return ans
# @lc code=end

