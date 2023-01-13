#
# @lc app=leetcode.cn id=629 lang=python3
#
# [629] K个逆序对数组
#

# @lc code=start
# 动态规划-未压缩空间
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = int(1e9) + 7
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] - (dp[i - 1][j - i] if j >= i else 0)) % MOD
        return dp[n][k]


# @lc code=end

# 动态规划
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [1] + [0 for _ in range(k)]
#         for i in range(1, n + 1):
#             g = [0 for _ in range(k + 1)]
#             for j in range(k + 1):
#                 g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (dp[j - i] if j - i >= 0 else 0) + dp[j]
#                 g[j] %= MOD
#             dp = g
#         return dp[k]

# 记忆化DFS
# from functools import lru_cache

# class Solution:
#     @lru_cache(None)
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         if not (n > 1 and k > 0): return int(n > k)
#         return (self.kInversePairs(n, k - 1) + self.kInversePairs(n - 1, k) - (self.kInversePairs(n - 1, k - n) if k >= n else 0)) % MOD
solution = Solution()
print(solution.kInversePairs(1000, 1000))