#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#

# @lc code=start
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, cnt = 0, 0
        for i in range(n):
            if i >= k and nums[i - k] > 1:
                cnt ^= 1
            if nums[i] == cnt:
                if i + k > n:
                    return -1
                ans += 1
                cnt ^= 1
                nums[i] += 2
        return ans

# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         diff = [0 for _ in range(n + 1)]
#         ans, cnt = 0, 0
#         for i, num in enumerate(nums):
#             cnt += diff[i]
#             if (num + cnt) % 2 == 0:
#                 if i + k > n:
#                     return -1
#                 ans += 1
#                 cnt += 1
#                 diff[i + k] -= 1
#         return ans
# @lc code=end

