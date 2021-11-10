#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        ans = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(0, dp[i - 1])
            ans = max(ans, dp[i])
        return ans
# @lc code=end

