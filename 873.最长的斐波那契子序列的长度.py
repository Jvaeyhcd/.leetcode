#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
import collections
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = collections.defaultdict(lambda:2)

        ans = 0
        for i, num in enumerate(arr):
            for j in range(i):
                k = index.get(num - arr[j], -1)
                if k > -1 and k < j:
                    cand = dp[j * n + i] = dp[k * n + j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
# @lc code=end

