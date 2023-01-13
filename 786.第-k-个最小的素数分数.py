#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#

# @lc code=start
from typing import List

# 二分查找
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1

            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += (i + 1)
            
            if count == k:
                return [x, y]
            elif count < k:
                left = mid
            else:
                right = mid
        
# @lc code=end

