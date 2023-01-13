#
# @lc app=leetcode.cn id=2333 lang=python3
#
# [2333] 最小差值平方和
#

# @lc code=start
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [0] * n
        ans = 0
        for i in range(n):
            diff[i] = abs(nums1[i] - nums2[i])
            ans += diff[i] * diff[i]
        
        k = k1 + k2
        if sum(diff) <= k: return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i, v in enumerate(diff):
            ans -= v * v
            j = i + 1
            c = j * (v - diff[j])
            if c < k:
                k -= c
                continue
            v -= k // j
            return ans + (k % j) * (v - 1) * (v - 1) + (j - k % j) * v * v
# @lc code=end

