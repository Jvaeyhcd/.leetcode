#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        ans = []
        
        rows = []
        for i in range(m):
            for j in range(n):
                rows.append(mat[i][j])
                if len(rows) == c:
                    ans.append(rows + [])
                    rows = []
        
        return ans
# @lc code=end

