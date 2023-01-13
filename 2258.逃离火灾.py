#
# @lc app=leetcode.cn id=2258 lang=python3
#
# [2258] 逃离火灾
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def check(t: int) -> bool:
            # 当前新着火的点
            f = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1]
            fire = set(f)

            def spread_fire():
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x, y) not in fire:
                            fire.add((x, y))
                            f.append((x, y))
            
            while t and f:
                spread_fire()
                t -= 1
            
            if (0, 0) in fire:
                return True
            
            q = [(0, 0)]
            vis = set(q)
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.pop(0)
                    if i == m - 1 and j == n - 1:
                        return False
                    if (i, j) in fire:
                        continue
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x, y) not in fire and (x, y) not in vis:
                            q.append((x, y))
                            vis.add((x, y))
                spread_fire()
            
            return True

        ans = bisect_left(range(m * n + 1), True, key=check) - 1
        return ans if ans < m * n else 10**9

# @lc code=end

