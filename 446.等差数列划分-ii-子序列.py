#
# @lc app=leetcode.cn id=446 lang=python
#
# [446] 等差数列划分 II - 子序列
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in nums]
        for i in range(n):
            x = nums[i]
            for j in range(i):
                d = x - nums[j]
                cnt = dp[j][d]
                ans += cnt
                dp[i][d] += cnt + 1
        
        return ans
# @lc code=end

