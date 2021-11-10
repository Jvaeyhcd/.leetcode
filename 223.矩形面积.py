#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
# 简化版本
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x = max(0, min(ax2, bx2) - max(ax1, bx1))
        y = max(0, min(ay2, by2) - max(ay1, by1))
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - (x * y)
# @lc code=end

# 初中数学题
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def computeRectangleArea(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x2 - x1) * abs(y2 - y1)
        
        areaA = computeRectangleArea(ax1, ay1, ax2, ay2)
        areaB = computeRectangleArea(bx1, by1, bx2, by2)

        # b全部包含在a里面
        if ax1 <= bx1 <= ax2 and ax1 <= bx2 <= ax2 and ay1 <= by1 <= ay2 and ay1 <= by2 <= ay2:
            return areaA
        # a全部包含在b里面
        elif bx1 <= ax1 <= bx2 and bx1 <= ax2 <= bx2 and by1 <= ay1 <= by2 and by1 <= ay2 <= by2:
            return areaB
        else:
            # 计算共区域
            x, y = 0, 0
            if ax1 <= bx1 <= ax2:
                x = bx2 - bx1 if ax1 <= bx2 <= ax2 else ax2 - bx1
            elif bx1 <= ax1 <= bx2:
                x = ax2 - ax1 if bx1 <= ax2 <= bx2 else bx2 - ax1
            if ay1 <= by1 <= ay2:
                y = by2 - by1 if ay1 <= by2 <= ay2 else ay2 - by1
            elif by1 <= ay1 <= by2:
                y = ay2 - ay1 if by1 <= ay2 <= by2 else by2 - ay1
            return areaA + areaB - x * y