#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            rows = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    rows.append(1)
                else:
                    rows.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(rows)
        return ans

# @lc code=end

