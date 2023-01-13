#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q = []
        curFuel = startFuel
        ans = 0
        i = 0
        while curFuel < target:
            if i < len(stations) and curFuel >= stations[i][0]:
                heapq.heappush(q, -stations[i][1])
                i += 1
            else:
                if q:
                    curFuel -= heapq.heappop(q)
                    ans += 1
                else:
                    return -1
        return ans
# @lc code=end

s = Solution()
# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
target = 100
startFuel = 50
stations = [[40,50]]
print(s.minRefuelStops(target, startFuel, stations))