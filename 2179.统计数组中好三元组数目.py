#
# @lc app=leetcode.cn id=2179 lang=python3
#
# [2179] 统计数组中好三元组数目
#

# @lc code=start
import collections
from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.bit_arr = [0 for _ in range(n + 1)]
    
    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int):
        n = len(self.bit_arr)
        while idx < n:
            self.bit_arr[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        ans = 0
        while idx:
            ans += self.bit_arr[idx]
            idx -= self.lowbit(idx)
        return ans

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        BIT = FenwickTree(n)
        mp = collections.defaultdict(int)
        for i, num in enumerate(nums2):
            mp[num] = i + 1

        ans = 0
        for i in range(n):
            index = mp[nums1[i]]
            a = BIT.query(index)
            b = n - index - (BIT.query(n) - a)
            ans += (a * b)
            BIT.update(index, 1)
        return ans
# @lc code=end

