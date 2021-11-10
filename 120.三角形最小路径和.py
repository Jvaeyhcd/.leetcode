#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start

# 动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for row in range(1, n):
            for col in range(row + 1):
                if col == 0:
                    dp[row][col] = dp[row - 1][col]
                elif col == row:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1])
                dp[row][col] += triangle[row][col]
        return min(dp[n - 1])

# @lc code=end

# 记忆化DFS
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        self.memo = collections.defaultdict(lambda:collections.defaultdict(int))
        self.memo[0][0] = triangle[0][0]
        
        def dfs(row: int, col: int):
            if col in self.memo[row]:
                return self.memo[row][col]
            
            ans = 0
            if col == 0:
                ans = dfs(row - 1, col)
            elif col == row:
                ans = dfs(row - 1, col - 1)
            else:
                ans = min(dfs(row - 1, col), dfs(row - 1, col - 1))
            
            ans += triangle[row][col]
            self.memo[row][col] = ans
            return ans
        
        n = len(triangle)
        return min([dfs(n - 1, i) for i in range(n)])