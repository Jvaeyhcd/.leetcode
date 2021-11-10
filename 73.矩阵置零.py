#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
# O(m+n)空间
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in rows:
            for c in range(n):
                matrix[r][c] = 0
        for c in cols:
            for r in range(m):
                matrix[r][c] = 0


# @lc code=end
