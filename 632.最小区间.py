#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left, right = -10**6, 10**6
        max_value = max(a[0] for a in nums)
        pq = [(a[0], i, 0) for i, a in enumerate(nums)]
        heapq.heapify(pq)
        while True:
            min_value, i, j = heapq.heappop(pq)
            if max_value - min_value < right - left:
                left, right = min_value, max_value
            if j == len(nums[i]) - 1:
                break
            max_value = max(max_value, nums[i][j + 1])
            heapq.heappush(pq, (nums[i][j + 1], i, j + 1))
        return [left, right]
# @lc code=end

