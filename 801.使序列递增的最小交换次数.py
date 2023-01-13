#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

# @lc code=start
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = [0, 1]
        for i in range(1, n):
            p = f
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                p[0] = f[0]
                p[1] = f[1] + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                p[0] = min(p[0], f[1])
                p[1] = min(p[1], f[0] + 1)
            f = p
            print(f)
        print(f)
        return min(f)
# @lc code=end

solution = Solution()
nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
print(solution.minSwap(nums1, nums2))