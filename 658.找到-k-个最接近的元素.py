#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect_left(arr, x)
        n = len(arr)
        if pos + 1 < n and abs(arr[pos] - x) > abs(arr[pos + 1] - x):
            pos = pos + 1
        l, r = pos, pos
        i = 0
        ans = []
        while i < k:
            if l < 0 and r >= n:
                break
            if l < 0 or (r < n and abs(arr[r] - x) < abs(arr[l] - x)):
                ans.append(arr[r])
                r += 1
            else:
                if l == r:
                    r += 1
                ans.insert(0, arr[l])
                l -= 1
            i += 1
        return ans
# @lc code=end

