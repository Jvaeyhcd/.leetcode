#
# @lc app=leetcode.cn id=2402 lang=python3
#
# [2402] 会议室 III
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        pq1 = [i for i in range(n)]
        pq2 = []
        cnts = [0] * n
        meetings.sort()

        for start, end in meetings:
            while pq2 and pq2[0][0] <= start:
                _, room = heappop(pq2)
                heappush(pq1, room)
            if pq1:
                r = heappop(pq1)
                heappush(pq2, (end, r))
                cnts[r] += 1
            else:
                t, r = heappop(pq2)
                heappush(pq2, (t - start + end, r))
                cnts[r] += 1

        ans = mx = 0
        for i in range(n):
            if cnts[i] > mx:
                mx = cnts[i]
                ans = i
        return ans

# @lc code=end

