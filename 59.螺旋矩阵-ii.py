#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        
        circle = 0
        max_circle = n / 2 if n % 2 == 0 else n / 2 + 1
        while circle < max_circle:
            # 上面一行
            for i in range(circle, n - circle):
                ans[circle][i] = num
                num += 1
            # 右边一行
            for i in range(circle + 1, n - circle - 1):
                ans[i][n - circle - 1] = num
                num += 1

            if circle != n - circle - 1:
                # 下面一行
                for i in range(n - circle - 1, circle - 1, -1):
                    ans[n - circle - 1][i] = num
                    num += 1
            if circle != n - circle - 1:
                # 左边一行
                for i in range(n - circle - 2, circle, -1):
                    ans[i][circle] = num
                    num += 1
            
            circle += 1
        
        return ans
# @lc code=end

