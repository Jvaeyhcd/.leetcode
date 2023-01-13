#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1
        d = sum(nums2) - sum(nums1)
        if d < 0:
            d = -d
            nums1, nums2 = nums2, nums1
        
        ans = 0
        cnts = Counter(6 - x for x in nums1) + Counter(x - 1 for x in nums2)
        for i in range(5, 0, -1):
            if i * cnts[i] >= d:
                return ans + (d + i - 1) // i
            ans += cnts[i]
            d -= i * cnts[i]
# @lc code=end

