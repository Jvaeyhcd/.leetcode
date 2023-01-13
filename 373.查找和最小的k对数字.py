#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        heapq.heapify(pq)
        ans = []
        while pq and len(ans) < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
# @lc code=end

