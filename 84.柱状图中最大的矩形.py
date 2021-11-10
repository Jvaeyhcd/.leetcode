#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        area = 0
        heights = [0] + heights + [0]
        n += 2
        stack = [0]
        
        for i in range(1, n):
            while heights[stack[-1]] > heights[i]:
                height = heights[stack.pop(-1)]
                width = i - stack[-1] - 1
                area = max(area, width * height)
            stack.append(i)

        return area
# @lc code=end

