#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            idx = bisect_left(stack, num)
            if idx == len(stack):
                stack.append(num)
            else:
                stack[idx] = num
        return len(stack)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)
# @lc code=end

