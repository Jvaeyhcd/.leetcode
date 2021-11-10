#
# @lc app=leetcode.cn id=918 lang=python
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        max_val = nums[0]
        min_val = 0
        max_dp[0] = nums[0]
        min_dp[0] = 0
        sum_val = nums[0]
        for i in range(1, n):
            sum_val += nums[i]
            max_dp[i] = nums[i] + max(0, max_dp[i - 1])
            min_dp[i] = nums[i] + min(0, min_dp[i - 1])
            max_val = max(max_val, max_dp[i])
            min_val = min(min_val, min_dp[i])
        
        return max(sum_val - min_val, max_val)
# @lc code=end

