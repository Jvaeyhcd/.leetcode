#
# @lc app=leetcode.cn id=1606 lang=python3
#
# [1606] 找到处理最多请求的服务器
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heapq.heappop(busy)
                heapq.heappush(available, i + (id - i) % k)
            if available:
                id = heapq.heappop(available) % k
                requests[id] += 1
                heapq.heappush(busy, (start + t, id))
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]
# @lc code=end

