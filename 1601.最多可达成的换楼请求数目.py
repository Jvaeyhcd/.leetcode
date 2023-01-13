#
# @lc app=leetcode.cn id=1601 lang=python3
#
# [1601] 最多可达成的换楼请求数目
#

# @lc code=start
import collections
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0 for _ in range(n)]
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] -= 1
                    delta[y] += 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans

# @lc code=end

