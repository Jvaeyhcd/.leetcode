#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        left, right = 0, N - 1
        ans = 0
        while left < right:
            w = right - left
            h = min(height[right], height[left])
            ans = max(ans, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end

