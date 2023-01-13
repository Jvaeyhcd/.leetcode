#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] 骑士在棋盘上的概率
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp[i][j]表示当前状态下骑士出现在坐标i,j位置的概率
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1
        for _ in range(k):
            f = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for ni, nj in [[i - 2, j + 1], [i - 2, j - 1], [i + 2, j + 1], [i + 2, j - 1], [i + 1, j - 2], [i - 1, j - 2], [i + 1, j + 2], [i - 1, j + 2]]:
                        if 0 <= ni < n and 0 <= nj < n:
                            f[ni][nj] += dp[i][j] * 0.125
            dp = f
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += dp[i][j]
        return ans


# @lc code=end

S = Solution()
n = 20
k = 90
row = 0
column = 0
print(S.knightProbability(n, k, row, column))