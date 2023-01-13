#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#

# @lc code=start
import functools


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        
        @functools.lru_cache(None)
        def dfs(mask: int, cur: int):
            
            for i in range(1, maxChoosableInteger + 1):
                if mask & (1 << i) == 0:
                    if cur + i >= desiredTotal or not dfs(mask | (1 << i), cur + i):
                        return True
            return False
        
        return dfs(0, 0)

# @lc code=end

maxChoosableInteger = 10
desiredTotal = 40
S = Solution()
print(S.canIWin(maxChoosableInteger, desiredTotal))