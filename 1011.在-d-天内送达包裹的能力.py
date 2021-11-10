#
# @lc app=leetcode.cn id=1011 lang=python
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            
            if need <= D:
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end

