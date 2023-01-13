#
# @lc app=leetcode.cn id=2040 lang=python3
#
# [2040] 两个有序数组的第 K 小乘积
#

# @lc code=start
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = [n1 * n2 for n1 in nums1 for n2 in nums2]
        # print(arr)
        arr = sorted(arr)
        return arr[k - 1]
# @lc code=end

[-2,-1,0,1,2]
[-3,-1,2,4,5]
3