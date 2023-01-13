#
# @lc app=leetcode.cn id=1997 lang=python3
#
# [1997] 访问完所有房间的第一天
#

# @lc code=start
import collections
import queue
from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9+7
        n = len(nextVisit)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            dp[i] = (dp[i - 1] * 2 - dp[nextVisit[i - 1]] + 2) % MOD
        return (dp[n - 1] - 1) % MOD
# @lc code=end

s = Solution()
nextVisit = [0,1,2,0]
nextVisit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.firstDayBeenInAllRooms(nextVisit))