#
# @lc app=leetcode.cn id=1296 lang=python3
#
# [1296] 划分数组为连续数字的集合
#

# @lc code=start
from typing import Counter, List
import heapq


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        cnts = Counter(nums)
        keys = list(cnts.keys())

        groups, arr = [], []
        heapq.heapify(keys)
        while keys:
            top = heapq.heappop(keys)
            if not groups or groups[-1] + 1 == top:
                groups.append(top)
                cnts[top] -= 1
                if cnts[top] > 0: heapq.heappush(keys, top)
            else:
                arr.append(top)

            if len(groups) == k:
                for a in arr:
                    if cnts[a] > 0: heapq.heappush(keys, a)
                groups = []
                arr = []
        return True if not arr else False
# @lc code=end

