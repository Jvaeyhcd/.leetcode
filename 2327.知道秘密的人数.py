#
# @lc app=leetcode.cn id=2327 lang=python3
#
# [2327] 知道秘密的人数
#

# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            cur = 0
            for j in range(max(1, i - forget + 1), max(1, i - delay + 1)):
                cur += dp[j]
            dp[i] = cur % MOD
        return sum(dp[max(1, n - forget + 1):]) % MOD
# @lc code=end

