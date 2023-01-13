#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        diff = s - target
        if diff < 0 or diff % 2 != 0:
            return 0
        n = len(nums)
        neg = diff // 2
        dp = [[0 for _ in range(neg + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]
# @lc code=end
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         self.ans = 0

#         def backtrack(index: int, s: int):
#             if index == len(nums):
#                 if s == target:
#                     self.ans += 1
#             else:
#                 backtrack(index + 1, s + nums[index])
#                 backtrack(index + 1, s - nums[index])
        
#         backtrack(0, 0)
#         return self.ans

S = Solution()
nums = [25,18,47,13,45,29,15,45,33,19,39,15,39,45,17,21,29,43,50,10]
target = 25
nums = [31,4,45,3,44,49,28,6,22,24,40,25,13,46,17,10,2,38,25,15]
target = 25
print(S.findTargetSumWays(nums, target))