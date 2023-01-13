#
# @lc app=leetcode.cn id=918 lang=python
#
# [918] 环形子数组的最大和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        minn, maxn = 0, nums[0]
        min_val, max_val = 0, nums[0]
        for i in range(1, n):
            mini = min(0, minn) + nums[i]
            maxi = max(0, maxn) + nums[i]
            max_val = max(max_val, maxi)
            min_val = min(min_val, mini)
            maxn, minn = maxi, mini
        return max(max_val, sum(nums) - min_val)
# @lc code=end

