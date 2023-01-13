#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        dirs = [(-1, 1), (1, -1)]
        f = 0
        x, y = 0, 0
        ans = [mat[0][0]]
        while True:
            if x == m - 1 and y == n - 1:
                break
            if f == 0:
                xx, yy = x + dirs[f][0], y + dirs[f][1]
                if xx == -1 or yy == n:
                    f = 1
                    if y + 1 < n:
                        x, y = x, y + 1
                    elif x + 1 < m:
                        x, y = x + 1, y
                else:
                    x, y = xx, yy
                ans.append(mat[x][y])
            else:
                xx, yy = x + dirs[f][0], y + dirs[f][1]
                if xx == m or yy == -1:
                    f = 0
                    if x + 1 < m:
                        x, y = x + 1, y
                    elif y + 1 < n:
                        x, y = x, y + 1
                else:
                    x, y = xx, yy
                ans.append(mat[x][y])
        return ans

# @lc code=end

