#
# @lc app=leetcode.cn id=576 lang=python3
#
# [576] 出界的路径数
#

# @lc code=start
import functools

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        @functools.lru_cache(None)
        def dfs(x: int, y: int, step: int) -> int:
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if step == 0:
                return 0
            ans = 0
            for nx, ny in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                ans += (dfs(nx, ny, step - 1) % MOD)
            return ans % MOD
        return dfs(startRow, startColumn, maxMove)

# @lc code=end

