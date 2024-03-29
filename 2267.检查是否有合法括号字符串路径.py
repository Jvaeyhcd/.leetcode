#
# @lc app=leetcode.cn id=2267 lang=python3
#
# [2267] 检查是否有合法括号字符串路径
#

# @lc code=start
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        dp = [[set() for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = set([1 if grid[0][0] == '(' else -1])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                v = 1 if grid[i][j] == '(' else -1

                s = set()
                s1 = dp[i][j + 1]
                s2 = dp[i + 1][j]
                for a in s1.union(s2):
                    if v == 1 or a > 0:
                        s.add(a + v)

                dp[i + 1][j + 1] = s
        
        return any(a == 0 for a in dp[m][n])



# @lc code=end

solution = Solution()
grid = [["(","(",")","(",")","(","(",")","(","(",")",")",")",")",")","(",")","(","(",")","(","(",")",")",")",")",")","(","(","(","("],[")","(","(","(",")","(",")","(","(",")",")",")",")","(",")",")","(","(",")",")","(",")","(",")","(","(",")","(",")","(","("],[")",")","(","(",")","(","(",")",")",")",")","(","(",")",")","(",")","(",")",")","(","(","(",")",")",")","(",")",")","(",")"],["(","(",")","(",")","(","(",")","(","(","(",")",")","(",")","(",")",")",")",")",")",")","(","(",")","(",")","(",")","(","("],[")",")","(",")",")","(","(","(",")",")","(",")","(",")",")",")","(","(","(",")",")","(",")","(",")",")","(","(","(","(",")"],[")",")","(","(",")","(",")","(",")","(",")","(",")",")","(",")","(",")",")","(",")","(","(","(",")","(",")",")",")","(","("],[")","(","(","(","(","(","(",")",")","(","(",")","(",")",")","(",")",")",")","(","(","(",")","(","(",")",")","(",")","(",")"],[")",")","(","(","(","(","(","(","(",")",")","(","(","(","(","(","(","(","(","(","(","(","(",")",")","(","(",")",")","(",")"],["(",")",")",")","(","(",")",")",")",")","(",")",")","(",")",")","(","(","(","(","(","(","(",")",")","(","(",")",")","(","("],["(","(",")","(",")",")",")",")","(","(","(",")",")",")","(",")","(","(",")","(","(","(",")","(","(","(","(","(",")",")",")"],["(",")","(","(","(","(",")","(","(",")",")","(","(",")","(","(","(",")","(","(","(",")",")","(",")",")","(",")","(","(",")"],[")",")","(","(","(","(",")","(","(",")",")","(",")",")","(",")","(","(","(","(","(","(","(",")","(","(",")",")","(","(","("],["(",")",")",")","(",")","(","(","(",")",")",")","(",")","(",")",")","(","(","(","(",")","(",")",")",")",")",")",")","(","("],["(","(","(","(","(","(",")",")","(",")","(","(","(",")",")","(",")","(",")","(",")","(","(","(",")",")",")","(",")","(","("],["(",")",")",")",")","(","(",")",")",")",")",")",")","(","(",")","(",")",")","(",")","(",")",")",")","(","(",")","(","(","("],["(",")",")","(","(",")",")","(",")",")","(","(","(",")",")",")",")","(","(","(",")",")","(",")","(","(","(","(",")",")",")"],[")","(","(",")","(","(",")",")",")","(","(","(","(",")","(",")",")",")","(",")","(",")","(","(",")","(","(","(","(","(","("],["(",")","(",")","(","(",")",")",")",")",")","(","(",")",")","(",")","(",")",")",")",")","(","(","(",")","(",")","(",")",")"],["(",")","(",")",")",")","(","(","(",")","(",")","(","(",")",")","(",")","(",")","(",")","(","(","(","(","(",")","(",")","("],[")",")",")",")",")","(",")",")","(","(",")","(",")",")","(",")",")","(","(","(","(",")","(","(","(","(",")",")",")",")","("],[")","(","(","(","(","(",")","(",")",")",")",")","(","(","(",")",")","(",")",")","(","(","(","(","(","(",")",")","(","(","("],["(","(","(",")",")","(",")","(",")",")",")",")","(",")",")",")",")","(",")","(","(","(","(",")","(","(","(","(","(","(",")"]]
print(solution.hasValidPath(grid))