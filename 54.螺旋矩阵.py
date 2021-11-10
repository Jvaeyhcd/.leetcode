#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        circle = 0
        max_circle = min(m, n) / 2 if min(m, n) % 2 == 0 else min(m, n) / 2 + 1
        
        ans = []
        while circle < max_circle:
            # 上面一行
            for i in range(circle, n - circle):
                ans.append(matrix[circle][i])
            # 右边一行
            for i in range(circle + 1, m - circle - 1):
                ans.append(matrix[i][n - circle - 1])

            if circle != m - circle - 1:
                # 下面一行
                for i in range(n - circle - 1, circle - 1, -1):
                    ans.append(matrix[m - circle - 1][i])
            if circle != n - circle - 1:
                # 左边一行
                for i in range(m - circle - 2, circle, -1):
                    ans.append(matrix[i][circle])
            
            circle += 1
        return ans
        
# @lc code=end

