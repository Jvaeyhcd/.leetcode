#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
from typing import List

# 位运算
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         xor = 0
#         n = len(nums)
#         for i in range(n):
#             xor ^= nums[i]
#         for i in range(n + 1):
#             xor ^= i
#         return xor

# 数学方法
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)

# @lc code=end

