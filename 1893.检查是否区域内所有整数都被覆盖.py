#
# @lc app=leetcode.cn id=1893 lang=python
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        
        cur = 0
        for i in range(1, 51):
            cur += diff[i]
            if i >= left and i <= right and cur <= 0:
                return False
        return True
# @lc code=end

