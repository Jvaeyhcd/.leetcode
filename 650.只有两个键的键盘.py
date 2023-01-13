#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
import functools


class Solution:
    def minSteps(self, n: int) -> int:
        INF = 0xf3f3f3f3
        
        @functools.lru_cache(None)
        def dfs(a: int) -> int:
            if a < 2:
                return 0
            if a < 4:
                return a
            ans = INF
            for i in range(1, a // 2):
                if a % i == 0:
                    ans = min(ans, dfs(i) + a // i)
            return ans
        
        return dfs(n)
            
# @lc code=end

