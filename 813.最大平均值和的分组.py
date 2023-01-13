#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#

# @lc code=start
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        presum = [0] * (n + 1)
        for i, num in enumerate(nums):
            presum[i + 1] = presum[i] + num
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = presum[i + 1] / (i + 1)
        
        for j in range(2, k + 1):
            for i in range(j - 1, n):
                ans = 0
                for step in range(j - 2, i):
                    ans = max(ans, dp[step][j - 1] + (presum[i + 1] - presum[step + 1]) / (i - step))
                dp[i][j] = ans
        return dp[-1][-1]
# @lc code=end

