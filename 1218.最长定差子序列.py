#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#

# @lc code=start
from typing import List
import collections

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())
# @lc code=end

