#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def dfs(i: int) -> int:
            if i == -1:
                return 1
            return qiuckPow(dfs(i - 1), 10) * qiuckPow(a, b[i]) % MOD

        def qiuckPow(a: int, n: int) -> int:
            ans = 1
            a %= MOD
            while n:
                if n & 1:
                    ans = ans * a % MOD
                a = a * a % MOD
                ans %= MOD
                n >>= 1
            return ans
        
        return dfs(len(b) - 1)
# @lc code=end

