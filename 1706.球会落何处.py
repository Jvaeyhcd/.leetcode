#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#

# @lc code=start
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def solve(col: int) -> int:
            for row in range(m):
                if grid[row][col] == 1:
                    if col + 1 < n and grid[row][col + 1] == 1:
                        col += 1
                    else:
                        return -1
                elif grid[row][col] == -1:
                    if col - 1 >= 0 and grid[row][col - 1] == -1:
                        col -= 1
                    else:
                        return -1
            return col
        ans = []
        for col in range(n):
            ans.append(solve(col))
        return ans
# @lc code=end
solution = Solution()
grid = [[-1]]
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
print(solution.findBall(grid))